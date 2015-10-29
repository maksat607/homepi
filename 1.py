import RPi.GPIO as g 
import time 
import os
# not_executed = True while(True):
	# dt = list(time.localtime()) hour = dt[3] minute = dt[4]
	
	# if hour == 9 and minute == 54:
		# print hour, ' ', minute
led=37 
g.setmode(g.BOARD) 
g.setup(led,g.OUT) 
g.output(37,False)
try:
	while True:
		dt = list(time.localtime())
		hour = dt[3] 
		minute = dt[4]
		time.sleep(15)
		print hour, " : ",minute
		if hour==5 and minute==0:
			g.output(37,True)
		#	os.system("bash -c mocp -G")
#			from subprocess import call
#			call(["mocp", "-G"])
except KeyboardInterrupt:
	g.cleanup()
