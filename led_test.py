from gpiozero import LED
from time import sleep

green = LED(16)
orange = LED(20)
red = LED(21)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
