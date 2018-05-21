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

#function to check the prompt and exit out from router

def Exit_Prompt(connection):

	if connection.check_config_mode():
		connection.exit_config_mode()
	
	if connection.check_enable_mode():
		connection.exit_enable_mode()
# Calls the csv_dict_list function, passing the named csv
device_list_csv='device_list.csv' 
device_dictonery=csv_dict_list(device_list_csv)

#pprint.pprint(device_dictonery)

#calling the connect handler with device list and entering router

connection=ConnectHanler(**device_dictonery)

Exit_Prompt(connection)

# passing the value to exit prompt

prompt=connection.find_prompt()
print(prompt)

# Extracting information from router about Interface 

show_ip_interface=connection.send_command('show ip interface brief')

#spliting the output from router 

interfaces=show_ip_interface.splitlines()

#turning on the interface

for interface in interfaces:
	all_interface=interface.split()
	if all_interface[5]=='down':
		print(all_interfaces[0]+'is Down')
		connection.enable()
		connection.config_mode()
		connection.send_config_set(['int'+all_interface[0],'noshut'])
		Exit_Prompt(connection)
		print('running final status')





