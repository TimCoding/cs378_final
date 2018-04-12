import subprocess
import re
from subprocess import check_output

#Runs ifconfig and gets ip address so NMAP can be performed
def runIfconfig():
	#command = "ifconfig | grep -Eo -m 1 '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1"
	ifcon = check_output(['ifconfig'])
	ifconResult = ifcon.decode("utf-8");
	regex = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
	ipaddress = regex.search(ifconResult)
	return ipaddress.group(0)

def runNMAP():
	ipaddress = runIfconfig() + "-30";
	# print(ipaddress)
	nmapResult = check_output(['nmap', ipaddress])
	print(nmapResult.decode("utf-8"))
