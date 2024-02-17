from netmiko import ConnectHandler

#First create the device object using a dictionary
R2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.1.2',
	'username': 'admin',
	'password': 'pass123',
	'secret': 'cisco'
}

#Part 1 New code
backup_file = input("Enter the name of the back up file to restore: ")

with open(backup_file, 'r') as file:
	backup_config = file.read()	

#Establish SSH connection
net_connect =  ConnectHandler(**R2)

#Part 2 New Code
net_connect.enable()
net_connect.config_mode()

output = net_connect.send_command_timing(backup_config)

print("Configuration restored")

net_connect.exit_config_mode()

#Finally close the connection
