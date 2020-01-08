import napalm
import json

class iosxenapalmapi(object):
    def __init__(self, hostname=None, username=None, password=None, optional_args=None):
        driver = napalm.get_network_driver('ios')
        # driver = napalm.get_network_driver('nxos_ssh')
        # driver = napalm.get_network_driver('ios-xr')
        self.connection = driver(hostname=hostname, username=username, password=password, optional_args={'port':8181})


    def connect(self):
        self.connection.open()

    def disconnect(self):
        self.connection.close()



    def get_facts(self):
        """Retrieve and return network devices informatiom.

            ./iosxenapalmapi.py get_facts
        """
        self.connect()
        facts = self.connection.get_facts()
        self.disconnect()
        return facts

    # def get_interfaces(self):
    #     """Retrieve and return network devices informatiom.
    #         ./iosxenapalmapi.py get_interfaces
    #     """
    #     self.connect()
    #     facts = self.connection.get_interfaces()
    #     self.disconnect()
    #     return facts

# devices
# hostname, username, password
# This example uses the always on devnet sandbox's ios xe, nx-os
device = iosxenapalmapi("sbx-nxos-mgmt.cisco.com", "admin", "Admin_1234!")
# device = iosxenapalmapi("ios-xe-mgmt.cisco.com", "root", "D_Vay!_10&")
# device = iosxenapalmapi("sbx-iosxr-mgmt.cisco.com", "admin", "C1sco12345")
# device = iosxenapalmapi("ios-xe-mgmt-latest.cisco.com","developer","C1sco12345")


# device = iosxenapalmapi("ios-xe-mgmt.cisco.com", "root", "D_Vay!_10&")
# print(device.get_facts())
print(json.dumps(device.get_facts(), sort_keys=True, indent=4))
# print(json.dumps(device.get_interfaces(), sort_keys=True, indent=4))
