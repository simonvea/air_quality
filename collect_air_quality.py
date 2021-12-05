#!/usr/bin/python3

from sgp30 import SGP30
import time
from datetime import datetime
import sys
from save_to_csv import saveAirQualityToCSV as saveLocally
from influx_db import saveToDb
from air_lights import refreshLights

sgp30 = SGP30()

arguments = sys.argv
useLocalDb = len(arguments) > 1 and (arguments[1] == 'local' or arguments[1] == '-l')
useLights = True

# result = sgp30.command('set_baseline', (0xFECA, 0xBEBA))
# result = sgp30.command('get_baseline')
# print(["{:02x}".format(n) for n in result])

print("Sensor warming up, please wait...")


def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()


sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')


def average(data):
    return round(sum(data) / len(data))

def saveData(eCO2, TVOC, room = "office"):
    try:
        if(useLocalDb):
            saveLocally(eCO2, TVOC)
        else:
            saveToDb(eCO2, TVOC, room)
    except:
        print("Error saving data! Ignoring the error for now")


latestCO2 = []
latestTVOC = []

print("Started measurement")

while True:
    result = sgp30.get_air_quality()
    latestCO2.append(result.equivalent_co2)
    latestTVOC.append(result.total_voc)
    if len(latestCO2) > 59:
        before = datetime.now()
        eCO2 = average(latestCO2)
        TVOC = average(latestTVOC)
        saveData(eCO2, TVOC)
        if(useLights):
            refreshLights(eCO2, TVOC)
        latestCO2.clear()
        latestTVOC.clear()
        after = datetime.now()
        difference = after - before
        if(difference.total_seconds() < 1.0):
            time.sleep(1.0 - difference.total_seconds())
        continue
    time.sleep(1.0)
