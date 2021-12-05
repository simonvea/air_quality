
from gpiozero import LED
import atexit

green = LED(16)
orange = LED(20)
red = LED(21)

#All are max for that area
TVOC_MODERATE = 660
TVOC_GOOD = 250
CO2_MODERATE = 2000
CO2_GOOD = 1000

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


def refreshLights(eCO2, TVOC):
    if(eCO2 > CO2_MODERATE or TVOC > TVOC_MODERATE):
        turnOnRed()
    elif(eCO2 > CO2_GOOD or TVOC > TVOC_GOOD):
        turnOnOrange()
    else:
        turnOnGreen()


def exitHandler():
    print("Turning off!")
    green.off()
    orange.off()
    red.off()


atexit.register(exitHandler)
