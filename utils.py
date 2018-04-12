import subprocess
from subprocess import check_output

#Runs ifconfig and gets ip address so NMAP can be performed
def runIfconfig():
	#command = "ifconfig | grep -Eo -m 1 '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1"
	grepCommand = "grep -Eo -m 1 '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'"
	headCommand = "head -1"
	grepCommandArray = grepCommand.split(' ')
	ifcon = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)
	grep = check_output(grepCommandArray, stdin=ifcon.stdout)
	ifcon.wait()
	print(grep)
	# grep.wait()
	# grabHead = check_output(headCommand.split(' '), stdin=grep.stdout)
	# result = grabHead.decode("utf-8")
	# print(result)
	# print("hello")
