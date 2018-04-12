from subprocess import check_output

#Runs ifconfig and gets ip address so NMAP can be performed
def runIfconfig():
	command = "ifconfig | grep -Eo -m 1 '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1"
	commandArray =  command.split(' ')
	result = check_output(command).decode("utf-8")
	print(result)
