import sys
import psutil
import time
from StatusLog import StatusLog
from ProcessList import ProcessList
import FilesHandler

class process_monitor:

	__delay = 0
	_ProcessList=None
	_StatusLog=None
    	
	def __init__(self, delay): # define process_monitor object with delay input
		self.__delay=delay
		self._ProcessList=ProcessList()
		self._StatusLog=StatusLog()

	def start(self):	#start process monitor
		observer =FilesHandler.Observer()
        	observer.schedule(FilesHandler.MyHandler(), '.')
		observer.start()
		while(1):
			Current_psutil = psutil
			self._ProcessList.write(Current_psutil,time.ctime())
			self._StatusLog.write(Current_psutil,time.ctime())	
           	 	time.sleep(self.__delay)


###############################              start the program           ###############################          
x = input("Enter the delay of scaning: ")
m = process_monitor(x)
m.start()


