import json
import napalm


class iosxenapalmapi(object):
    def __init__(self, driver=None, hostname=None, username=None, password=None, port=22):
        self.driver = driver
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.hostname)

    def _execute_call(self, driver, hostname, data=None):
        try:
            device_call = '{0}:{1}'(self.driver, self.hostname, self.port)
        except:
            print ("This is an error message!")


    def get_device(self):
        driver = napalm.get_network_driver('ios')
        device_call = self._execute_call('driver', 'hostname')
        print('Opening ...')
        device.open()
        device.get_facts()
        print (get_facts())
        device.close()
