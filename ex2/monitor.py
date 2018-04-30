import psutil
import time
import datetime
from StatusLog import StatusLog
from ProcessList import ProcessList
import FilesHandler

class process_monitor:

	_ProcessList=None
	_StatusLog=None
    	
	def __init__(self): # define process_monitor object with delay input
		self._ProcessList=ProcessList()
		self._StatusLog=StatusLog()

	def start_monitor(self,delay):	#start process monitor
		__delay =delay
		observer =FilesHandler.Observer()
        	observer.schedule(FilesHandler.MyHandler(), '.')
		observer.start()
		while(1):
			Current_psutil = psutil
			self._ProcessList.write(Current_psutil,datetime.datetime.now().strftime("%y-%m-%d %H-%M"))
			self._StatusLog.write(Current_psutil,time.ctime())	
           	 	time.sleep(__delay)

	def check_samples(self):  #check the difference between the sampels
       		good_input = False
       		while not good_input:
           		first_date = raw_input("Enter Date of sample (yy-mm-dd hh-mm): ")
           		try:  
                		userIn = datetime.datetime.strptime(first_date, "%y-%m-%d %H-%M")
               			good_input = True
           		except:
                		print "Input doesn't match the pattern, try again!\n"
        			good_input = False
		good_input = False
        	while not good_input:
          		second_date = raw_input("Enter Date of later sample (yy-mm-dd hh-mm): ")
            		try: 
                		userIn = datetime.datetime.strptime(second_date, "%y-%m-%d %H-%M")
                		good_input = True
            		except:
                		print "Input doesn't match the pattern, try again!\n"
				good_input=False
		first_sample = self._ProcessList.find_sample(first_date)
       		second_sample = self._ProcessList.find_sample(second_date)

		new_process = []
           	not_alive_process = []
            	for pid in second_sample:
                	if pid not in first_sample:
                    		new_process.append(pid)
          	for pid in first_sample:
               		if pid not in second_sample:
                  		not_alive_process.append(pid)
	
		if(new_process):
            		print('new processes:' + '\n')
            		for pid in new_process:
                		print("pid: "+str(pid))
		if(not_alive_process):
         		print('processes that not alive anymore:' + '\n')
            		for pid in not_alive_process:
                		print("pid: "+str(pid))


###############################              start the program           ############################### 
what_to_do=input("Enter 0 to start monitor OR enter 1 to check differences between samples\n")
if what_to_do==0:      
	x = input("Enter the delay of scaning: ")
	m = process_monitor()
	m.start_monitor(x)
elif what_to_do==1:
	m = process_monitor()
	m.check_samples()
	


