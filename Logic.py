import threading 
from threading import*
import time
import os.path
import json


d={}
fileName = "default.json"


def load(fname):
	global d
	global fileName
	if len(fname) != 0:
		fileName = fname	
		if os.path.exists(fileName):
			with open(fileName, 'r') as f:
				d = json.load(f)
		else:
			with open(fileName, 'w') as f:
				pass
	else:
		if os.path.getsize(fileName) != 0:
			with open(fileName, 'r') as f:
				d = json.load(f)

 
def read(key):
	global d
	global fileName
	if key not in d:
		print(key +" does not exist in database.") 
	else:
		load(fileName)
		b=d[key]
		if b[1]!=0:
			if time.time()<b[1]: 
				stri=str(key)+":"+str(b[0])
				print( stri )
			else:
				print(key," has been expired")
		else:
			stri=str(key)+":"+str(b[0])
			print( stri )
			
			
def create(key,value,timeout=0):
	global d
	global fileName
	if key in d:
		print("The key already exists in the Database")
	else:
		if(key.isalpha()):
			if len(d)<(1024*1024*1024) and len(value)<=(16*1024):
				if timeout==0:
					l=[value,timeout]
				else:
					l=[value,time.time()+timeout]
				if len(key)<=32:
					d[key]=l
					with open(fileName, 'w') as f:
						json.dump(d, f)
				
			else:
				print("error: Memory limit exceeded!! ")
		else:
			print("Invalid key")
			

def delete(key):
	global d
	global fileName
	if key not in d:
		print(key +" does not exist in database.") 
	else:
		b=d[key]
		if b[1]!=0:
			if time.time()<b[1]: 
				d.pop(key)
				with open(fileName, 'w') as f:
					json.dump(d, f)
				print("key is successfully deleted")
				load(fileName)
			else:
				print(key,"has been expired") 
		else:
			d.pop(key)
			with open(fileName, 'w') as f:
				json.dump(d, f)	
			load(fileName)
			print("key is successfully deleted")