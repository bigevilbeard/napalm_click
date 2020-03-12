# Network Automation with Napalm and Click Python libraries

Network automation and devices management has many paths and options... With so many APIs being available your network can quickly be as complex to manage with automation as it was with manual configurations. Evaluating the offerings of API vendors often goes past the technology itself. But, [NAPALM](https://napalm.readthedocs.io/en/latest/index.html) (Network Automation and Programmability Abstraction Layer with Multivendor support) is helping to change that, a unified API makes it possible to share code between network devices and vendors.

NAPALM is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.

[Click](https://click.palletsprojects.com/en/7.x/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.

## DevNet Sandbox
All code has been written/tested on the [Cisco DevNet IOS XR always on Sandbox](https://t.co/V6rXj3plwF).
Please see the sandbox pages for credentials and reservations.

## Code

All of the code you need is located in this repo. Clone the repo and access it with the following commands:

```
git clone https://github.com/bigevilbeard/napalm_click
cd napalm_click
```

## Python Environment Setup
It is recommended that this code be used with Python 3.6. It is highly recommended to leverage Python Virtual Environments (venv).

Follow these steps to create and activate a venv.
```
# OS X or Linux
virtualenv venv --python=python3.6
source venv/bin/activate
```
## Install the code requirements
```
pip install -r requirements.txt
```


## Running the code examples

NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data. Configurations can be replaced entirely or merged into the existing device config. You can load configuration either from a string or from a file. If for some reason you committed the changes and you want to rollback, this can also be done (please check NAPALM documentation for support of merge, replace and rollback as some platforms differ)


This code uses Object-Oriented Programming (OOP). This is a programming paradigm where different components of a computer program are modeled after real-world objects. An object is anything that has some characteristics and can perform a function. All args used in the running of the code are handled using [Click](https://click.palletsprojects.com/en/7.x/).

```
cli.add_command(facts)
cli.add_command(interfaces)
cli.add_command(interfaces_ip)
cli.add_command(merge)
cli.add_command(replace)
cli.add_command(rollback)

```
**Note:** Before using the code, update the IP address/hostname and port information.

```
(venv) STUACLAR-M-R6EU:napalm_click stuaclar$ python iosxenapalmapi.click.py --help
Usage: iosxenapalmapi.click.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  facts
  interfaces
  interfaces_ip
  merge
  replace
  rollback
  validation
```

With this code, we show the router version and interface information (shown in `json` format).



## Example Use Commands

```
(venv) STUACLAR-M-R6EU:napalm_click stuaclar$ python iosxenapalmapi.click.py interfaces
Retrieving Information
{
    "Loopback100": {
        "description": "",
        "is_enabled": true,
        "is_up": true,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 0
    },
    "Loopback200": {
        "description": "",
        "is_enabled": true,
        "is_up": true,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 0
    },
    "MgmtEth0/RP0/CPU0/0": {
        "description": "",
        "is_enabled": true,
        "is_up": true,
        "last_flapped": -1.0,
        "mac_address": "08:00:27:82:91:AB",
        "speed": 1000
    },
    "Null0": {
        "description": "",
        "is_enabled": true,
        "is_up": true,
        "last_flapped": -1.0,
        "mac_address": "",
        "speed": 0
    }
}
```
```
(venv) STUACLAR-M-R6EU:napalm_click stuaclar$ python iosxenapalmapi.click.py merge
Merge Loopback Interfaces

Diff:
---
+++
@@ -10,6 +10,12 @@
+!
+interface Loopback100
+ ipv4 address 1.1.1.100 255.255.255.255
+!
+interface Loopback200
+ ipv4 address 1.1.1.200 255.255.255.255
 !
 interface MgmtEth0/RP0/CPU0/0
  ipv4 address dhcp

Would you like to commit these changes? [yN]: y
Committing ...
```

## About me

Network Automation Developer Advocate for Cisco DevNet.
I'm like Hugh Hefner... minus the mansion, the exotic cars, the girls, the magazine and the money. So basically, I have a robe.

Find me here: [LinkedIn](https://www.linkedin.com/in/stuarteclark/) / [Twitter](https://twitter.com/bigevilbeard)
