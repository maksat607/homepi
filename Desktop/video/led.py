import RPi.GPIO as g
import time
import os

# not_executed = True

# while(True):
	# dt = list(time.localtime())
	# hour = dt[3]
	# minute = dt[4]
	
	# if hour == 9 and minute == 54:
		# print hour, ' ', minute
led=11
g.setmode(g.BOARD)
g.setup(led,g.OUT)
		# break

for x in range(0,3):
	g.output(led,True)     #g.output(11,g.LOW)
	time.sleep(1)
	g.output(led,False)
	time.sleep(1)
g.cleanup()