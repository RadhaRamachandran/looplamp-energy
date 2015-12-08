from bibliopixel import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
from bibliopixel.colors import colors

numLeds=26
driver=DriverLPD8806(numLeds)
led=LEDStrip(driver)