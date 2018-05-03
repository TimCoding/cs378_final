# ezWifi

A Python-based GUI tool to hack into nearby wireless networks and obtain network information as well as vulnerabilities.

## Getting Started

You need to first install Kivy for this to work. Detailed instructions are found on their website:

https://kivy.org/docs/installation/installation.html

These instructions are valid for Ubuntu, Windows, Mac OS X, and Mac OS X Homebrew. However, if you are trying to install this tool on Kali Linux, you need to enable PPA repositories:

https://www.blackmoreops.com/2014/02/21/kali-linux-add-ppa-repository-add-apt-repository/

Then, follow instructions for the Ubuntu distribution above.

Lastly, you'll need to install nmap, Python 3, pip, and git for this tool to work.

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