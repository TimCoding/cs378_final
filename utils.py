import subprocess
import re
from subprocess import check_output
import csv 
from itertools import islice

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

#target takes in a bssid
def runPasswordCracker(target):
	passwordCrackerCmd = "aircrack-ng -w /usr/share/john/password.lst -b " + target + " test-02.cap"
	passwordCrackerCmdArray = passwordCrackerCmd.split(' ')
	regex = re.compile(r'\[\s[a-zA-z\d]*\s\]')
	passwordCrackerResult = check_output(passwordCrackerCmdArray).decode("utf-8")
	password = regex.search(passwordCrackerResult)
	return password.group(0)

def read_bssid():
	with open("cs378-01.csv", 'r') as fp:
		reader = csv.reader(fp, delimiter=',', quotechar='"')
		next(reader, None)
		#data_read = [row for row in reader if len(row) == 15]
		data_channel = {}
		for row in islice(reader, 1, None):
			if len(row) == 15:
				channel = int(row[3])
				if 0 <= channel:
					if channel not in data_channel: 
						data_channel[channel] = []
					#name, bssid, channel
					if row[13] is not " ":
						data_channel[channel].append([str(len(data_channel[channel]))+ " " + row[13], row[0], row[3]])
		return data_channel[6]

def parse_num_ssid(name):
	regex = re.compile(r'([1-9]+)[\s]([a-zA-Z1-9]*)')
	num = int(regex.search(name).group(1))
	return num