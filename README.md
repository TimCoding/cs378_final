# ezWifi

A Python-based GUI tool to hack into nearby wireless networks and obtain network information as well as vulnerabilities.

## Getting Started

You need to first install Kivy for this to work. Detailed instructions are found on their website:

https://kivy.org/docs/installation/installation.html

These instructions are valid for Ubuntu, Windows, Mac OS X, and Mac OS X Homebrew. However, if you are trying to install this tool on Kali Linux, you need to enable PPA repositories:

https://www.blackmoreops.com/2014/02/21/kali-linux-add-ppa-repository-add-apt-repository/

Then, follow instructions for the Ubuntu distribution above.

Lastly, you'll need to install nmap, Python 3, pip, and git for this tool to work.

### Prerequisites for ezWifi main application

NOTE: It is HIGHLY recommended that you run the ezWifi main application (The GUI and everything outside the vulnerability_scan folder) on a Kali instance you have running on VirtualBox.  

You will need to make sure you have all the appropriate Python libraries to run the Kivy-based application. Once you have cloned this repository there are several Python libraries that need to be installed. Also make sure you have Python 3 on your Kali instance. 

- python3 -m pip install Pillow
- python3 -m pip install Kivy
- python3 -m pip install pygame 

In order to run the the main ezWifi program:

```
python3 networkcrack.py

```
To begin:

0.) Set up your wireless hacking device. NOTE: Program is set for your device to be wlan0mon once you do airmon-ng start <device> 
1.) Click the scan button and wait for the progress bar to finish
2.) Click refresh networks to display all networks you captured packets from
3.) Select a network you want to exploit
4.) Select a password strength you want (For submission purposes all password lengths are the same, only on our development machine was there different password lists) 
5.) Click Handshake and wait for progress bar
6.) Click crack password
7.) If a password was cracked it will be displayed
8.) Connect to the network you just gained access to
9.) Click scan network to run NMAP and look at data.txt generated in the directory to see NMAP results. 
10.) Use live hosts revealed in NMAP results to feed ip-addresses to vulnerability scanner in the folder vulnerability_scan

### Prerequisites

You need a compatible wireless network adapter, such as those made by Alfa or Panda. Specific chipsets will depend on your system and OS version.

Install the Python library requests by running:
```
pip install requests
```

Also, it is recommended that you have permission to do any sort of network scanning or wireless sniffing before you run this tool.

### Installing

vulscan is a set of nmap scripts, so first find where your nmap scripts are located by running the following command in a Terminal:

```
find / -name '*.nse'
locate *.nse
```

Find the file path, go to vulnerability_scan/Constants.py and replace the TO_DIRECTORY path string if need be.
Replace KIVY_COMMAND with your platform-specific way of running a Kivy file (eg. for Mac OS X it's "kivy").

Then, run the setup script:

```
python3 vulnerability_scan/setup.py
```

Also, run the update script every so often to keep the database recent:

```
python vulnerability_scan/update.py
```

## Usage

Run the Kivy GUI app by running Kivy on whichever platform you're on - for example, in Mac OS X:

```
kivy run.py
```

Optionally, to run the vulnerability GUI tool:

```
python3 vulnerability_scan/run.py <TARGET_IP>
```
