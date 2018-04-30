import time
import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

class StatusLog:

	__last_modified=None
	__Previos_Pids = []

	def write(self,__Current_psutil,__time):  #write the Status_Log.txt file
		Current_pids = __Current_psutil.pids()	
		new_process = []
           	not_alive_process = []
            	for pid in self.__Previos_Pids:
                	if pid not in Current_pids:
                    		not_alive_process.append(pid)
          	for pid in Current_pids:
               		if pid not in self.__Previos_Pids:
                  		new_process.append(pid)
            	self.__Previos_Pids = Current_pids
		if os.path.isfile('Status_Log.txt'):
			if self.__last_modified != os.stat('Status_Log.txt').st_mtime:
				print("worrning!! the file Status_Log.txt was change outside the program")
			os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
	        status_log_file = open('Status_Log.txt', 'a')
            	status_log_file.write('*' * 150 + '\n\n')
            	status_log_file.write(__time + '\n\n')
		if(new_process):
            		print('new processes:' + '\n')
            		status_log_file.write('new processes:' + '\n')
            		for pid in new_process:
                		print("pid: "+str(pid))
               			status_log_file.write("pid: "+str(pid) + '\n')
            	status_log_file.write('\n')
		if( not_alive_process):
         		print('processes that not alive anymore:' + '\n')
            		status_log_file.write('processes that not alive anymore:' + '\n')
            		for pid in not_alive_process:
                		print("pid: "+str(pid))
                		status_log_file.write("pid: "+str(pid) + '\n')
           	status_log_file.write('\n\n')
            	status_log_file.close()
		os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH) #readonly
		self.__last_modified = os.stat('Status_Log.txt').st_mtime
