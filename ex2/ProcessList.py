import time
import os
import csv
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

class ProcessList:

	__last_modified=None


	def write(self,__Current_psutil,__time): #write the processList.csv file
		if os.path.isfile('processList.csv'):
			if self.__last_modified != os.stat('processList.csv').st_mtime:
				print("worrning!! the file was processList.csv change outside the program")
			os.chmod('processList.csv', S_IWUSR | S_IREAD)
		list_of_process_file = open("processList.csv",'a')
		list_of_process_file.write("time"+','+"pid"+','+"name"+"\n")
            	for process in __Current_psutil.process_iter():
                	list_of_process_file.write(__time+','+str(process.pid)+','+str(process.name())+"\n")
           	list_of_process_file.close()
		os.chmod('processList.csv', S_IREAD | S_IRGRP | S_IROTH)	#readonly
		self.__last_modified=os.stat('processList.csv').st_mtime

	def find_sample(self, date):
        	result = []
       		with open('processList.csv', 'rb') as f:
            		reader = csv.reader(f)
			your_list = list(reader)
			for i in your_list:
               			if i[0] == date:
                    			result.append(i[1])
		return result


