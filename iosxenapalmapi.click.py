import napalm
import click
import json

class iosxenapalmapi(object):
    def __init__(self, hostname=None, username=None, password=None, optional_args=None):
        driver = napalm.get_network_driver('ios-xr')
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

    def get_interfaces(self):
        """Retrieve and return network devices informatiom.
            ./iosxenapalmapi.py get_interfaces
        """
        self.connect()
        facts = self.connection.get_interfaces()
        self.disconnect()
        return facts


device = iosxenapalmapi("sbx-iosxr-mgmt.cisco.com", "admin", "C1sco12345")

@click.group()
def cli():
    pass

@click.command()
def facts():
    click.secho("Retrieving Information")
    fact = json.dumps(device.get_facts(), sort_keys=True, indent=4)
    click.echo(fact)


@click.command()
def interfaces():
    click.secho("Retrieving Information")
    interface = json.dumps(device.get_interfaces(), sort_keys=True, indent=4)
    click.echo(interface)

cli.add_command(facts)
cli.add_command(interfaces)

if __name__ == "__main__":
    cli()
