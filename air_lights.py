from sgp30 import SGP30
from time import sleep
import sys
from gpiozero import LED
import atexit


sgp30 = SGP30()

# Only starts actual measurments after 15s of values.
# < 500 CO2 and < 50 TVOC is good air quality
#  500-100 CO2 is a little uncomfortable, 50-750 TVOC is uncomfortable
# 1000-2500 CO2 will make you tired, 750-6000 TVOC will lead to headache and depressive
# 2500-5000 CO2 is unhealthy, >6000 TVOC will lead to headache and other nerve problems

# result = sgp30.command('set_baseline', (0xFECA, 0xBEBA))
# result = sgp30.command('get_baseline')
# print(["{:02x}".format(n) for n in result])

print("Sensor warming up, please wait...")


def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()


sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')

green = LED(16)
orange = LED(20)
red = LED(21)

currentLight = 'green'
green.is_active


def turnOnGreen():
    if(red.is_active):
        red.off()
    if(orange.is_active):
        orange.off()
    if(green.is_active == False):
        green.on()


def turnOnOrange():
    if(red.is_active):
        red.off()
    if(green.is_active):
        green.off()
    if(orange.is_active == False):
        orange.on()


def turnOnRed():
    if(green.is_active):
        green.off()
    if(orange.is_active):
        orange.off()
    if(red.is_active == False):
        red.on()


def handleValues(eCO2, TVOC):
    if(eCO2 > 1000 or TVOC > 750):
        turnOnRed()
    elif(eCO2 > 500 or TVOC > 50):
        turnOnOrange()
    else:
        turnOnGreen()


def exitHandler():
    print("Turning off!")
    green.off()
    orange.off()
    red.off()


atexit.register(exitHandler)


while True:
    result = sgp30.get_air_quality()
    handleValues(result.equivalent_co2, result.total_voc)
    print(result)
    sleep(1.0)
