#Import the required libraries
import json
import time
import os
import threading
from threading import Thread

#This program uses the json.load and json.dumps functions that that are in-built in the json module to read and write to the json file
def read_from_json():
    with open(file+'.json', 'r+') as openfile:
         # Reading from json file 
         json_object = json.load(openfile)

def write_to_json():
    with open(file+'.json', 'w+') as openfile:
         # Writing to json file 
         openfile.write(json.dumps(json_object,indent=1))
    openfile.close()
    
def time_to_live(t,key):
    #defining the optional time to live property
    #this timer will run in a separate thread
    delay=threading.Timer(t,deleterec,[key])
    delay.start()
    print("Record with key",key," will be deleted after ",t," seconds")
    
def create():
    #function to create records
    key=input("Enter the key")  
    read_from_json()
    if(key in json_object):
       print("Datastore already has similar key.Please choose something else!")
       operations()
    else:
        data=input("Enter the json object(in json format)")
        #We can get json ojects directly from the client and parse it through the loads function
        #or we can get the data one by one and convert it into json format ourselves
        json_object.update({key:json.loads(data)})
        write_to_json()
        print("The values have been uploaded to the Datastore")    
        timer=input("Do you wish to set a time-to-live property for this record?(yes/no)")
        if(timer=="yes"):
            t=int(input("Enter time in seconds"))
            time_to_live(t,key)

def read():
    #This function takes a key as the input and prints the associated json object 
    print("Enter the key")
    key=input()
    read_from_json()
    if(key not in json_object):
        print("No such key found.Please enter a valid key!")
        operations()
    else:
        print(json_object[key])
    openfile.close()

def delete():
    #This function pops the key with the json object associated with it
    print("Enter the key")
    key=input()
    read_from_json()
    if(key not in json_object):
        print("No such key found.Please enter a valid key")
        operations()
    else:
        json_object.pop(key)
        #Dictionary is updated and written to file
        write_to_json()
        print("Record has been deleted from the Datastore")
        
def deleterec(key):
    #This function is specifically used to delete dictionary elements that have the time to live property
    read_from_json()
    if(key in json_object.keys()):
         json_object.pop(key)
    write_to_json()
    openfile.close()

def operations():
    #This function is created to enable recursion
    print("What do you want to do?\nPress 1 to CREATE a record\nPress 2 to READ an existing record\nPress 3 to DELETE an existing record\nPress 4 to EXIT")
    option=int(input())
    
    if(option==1):
        create()
        operations()
        
    if(option==2):
        read()
        operations()
        
    if(option==3):
        delete()
        operations()
        
    if(option==4):
        exit

        
#If file.json exists, the data store will be stored there
#Else, a json file with the given name will be created
file=input("Enter the file name in which the data store should be made available:")
#Checking if file exists and is not empty
if(os.path.isfile(file+'.json') and os.path.getsize(file+'.json')>0):
    with open(file+'.json', 'r+') as openfile:
         # Reading from json file 
         json_object = json.load(openfile)
    openfile.close()
    operations()
else:
    #Inintializing the file with some values
    with open(file+'.json', 'w+') as openfile:
        dictionary={"Key":"Json Object"}
        json_object = json.dumps(dictionary, indent = 4)
        openfile.write(json_object)
        openfile.close()
        with open(file+'.json', 'r+') as openfile:
         # Reading from json file 
             json_object = json.load(openfile)

    openfile.close()
    operations()
    
