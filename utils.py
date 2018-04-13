import subprocess
import re
from subprocess import check_output

#Runs ifconfig and gets ip address so NMAP can be performed
def runIfconfig():
	#command = "ifconfig | grep -Eo -m 1 '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1"
	ifcon = check_output(['ifconfig'])
	ifconResult = ifcon.decode("utf-8");
	#regex = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
	regex = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.')
	ipaddress = regex.search(ifconResult)
	return ipaddress.group(0)

def runNMAP():
	ipaddress = runIfconfig() + "1-30";
	# print(ipaddress)
	nmapResult = check_output(['nmap', ipaddress])
	print(nmapResult.decode("utf-8"))

def runPasswordCracker(target):
	passwordCrackerCmd = "aircrack-ng -w /usr/share/john/password.lst -b " + target + " test-02.cap"
	passwordCrackerCmdArray = passwordCrackerCmd.split(' ')
	regex = re.compile(r'\[\s[a-zA-z\d]*\s\]')
	passwordCrackerResult = check_output(passwordCrackerCmdArray).decode("utf-8")
	password = regex.search(passwordCrackerResult)
	print(password.group(0))
