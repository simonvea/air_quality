#!/usr/bin/python3

from sgp30 import SGP30
import time
from datetime import datetime
import sys
from save_to_csv import saveAirQualityToCSV as saveLocally
from influx_db import saveToDb

sgp30 = SGP30()


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


latestCO2 = []
latestTVOC = []

while True:
    result = sgp30.get_air_quality()
    latestCO2.append(result.equivalent_co2)
    latestTVOC.append(result.total_voc)
    if len(latestCO2) > 59:
        before = datetime.now()
        saveToDb(average(latestCO2), average(latestTVOC))
        latestCO2.clear()
        latestTVOC.clear()
        after = datetime.now()
        difference = after - before
        time.sleep(1.0 - difference.total_seconds())
        continue
    time.sleep(1.0)
