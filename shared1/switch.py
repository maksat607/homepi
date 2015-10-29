import RPi.GPIO as g
import os
import time
g.setmode(g.BOARD)
 
g.setwarnings(False)
g.setup(11,g.IN)
 
print '=================================='
print 'button'
print '=================================='

print g.input(11)
while True:
	if(g.input(11)==True):
		print('Button pressed')
		os.system('date')
		print g.input(11)
		time.sleep(3)
		
	else:
		os.system('clear')
		print ('waiting for you to press the button')
time.sleep(1)
g.cleanup()