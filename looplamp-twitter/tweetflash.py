import time
import json
from ledsetup import *

red=(0,255,0)
blue=(0,0,255)
green=(255,0,0)

def flash(delay, color):
	led.fill(color)
	led.update()
	time.sleep(delay)
	led.all_off()
	led.update()
	return



fname = 'twitter_out.json'
total=0
i=0
while i < 10: 
    num = sum(1 for line in open(fname))
    if num > total: 
        print("NEW TWEET!") # insert code here to flash the 
        print(num-total)
		flash(0.5,blue)
        total = num
        
        
    time.sleep(2)
    i+=1
    print(i)