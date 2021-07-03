
from gpiozero import LED
import atexit

green = LED(16)
orange = LED(20)
red = LED(21)

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
