#!/usr/bin/env python

 



#importing connecthandler to telnet or connect with router

from netmiko import ConnectHandler
import csv
import sys
import pprint



#dictonery created and providing the info about device
cisco_1700{ 
'Device_type':'cisco_ios_telnet',
'ip':'192.168.11.1',
'port':'2001',
'username':'root',
'password':'cisco'
}

# Function to convert a csv file to a list of dictionaries.
 
def csv_dict_list(device_list):
	reader = csv.DictReader(open(device_list, 'rb'))
	empty_list = []
	for line in reader:
		empty_list.append(line)
	return empty_list
 
# Calls the csv_dict_list function, passing the named csv
device_list_csv='device_list.csv' 
device_dictonery=csv_dict_list(device_list_csv)

#pprint.pprint(device_dictonery)

#checking the prompt and exit out if in ConfigT
def Exit_Prompt(connection):

	if connection.check_config_mode():
		connection.exit_config_mode()
	
	if connection.check_enable_mode():
		connection.exit_enable_mode()


