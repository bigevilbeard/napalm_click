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
        self.connect()
        facts = self.connection.get_facts()
        self.disconnect()
        return facts

    def get_validation(self):
        self.connect()
        facts = self.connection.compliance_report("validate.yml")
        self.disconnect()
        return facts

    def get_interfaces(self):
        self.connect()
        facts = self.connection.get_interfaces()
        self.disconnect()
        return facts

    def get_interfaces_ip(self):
        self.connect()
        facts = self.connection.get_interfaces_ip()
        self.disconnect()
        return facts

    def merge_loopbacks(self):
        self.connect()
        facts = self.connection.load_merge_candidate(filename='new_loopbacks.cfg')
        print('\nDiff:')
        diff = self.connection.compare_config()
        print(diff)
        if len(diff) < 1:
            print('\nNo Changes Required Closing...')
            self.connection.discard_config()
            self.disconnect()
            exit()

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        except NameError:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            self.connection.commit_config()

        else:
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()

    def replace_loopbacks(self):
        self.connect()
        facts = self.connection.load_replace_candidate(filename='replace.conf')
        print('\nDiff:')
        diff = self.connection.compare_config()
        print(diff)
        if len(diff) < 1:
            print('\nNo Changes Required Closing...')
            self.connection.discard_config()
            self.disconnect()
            exit()

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        except NameError:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            self.connection.commit_config()
            self.disconnect()

        else:
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()


    def rollback_loopbacks(self):
        self.connect()
        facts = self.connection.load_merge_candidate(filename='rollback_loopbacks.cfg')
        print('\nDiff:')
        diff = self.connection.compare_config()
        print(diff)
        if len(diff) < 1:
            print('\nNo Changes Required Closing...')
            self.connection.discard_config()
            self.disconnect()
            exit()

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        except NameError:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            self.connection.commit_config()

        else:
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()
            exit()

        choice = input("\nWould you like to rollback these changes? [yN]: ")
        if choice == 'y':
            print('Reverting ...')
            self.connection.rollback()
            self.disconnect()

        else:
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()

# hostname, username, password
# device = iosxenapalmapi("127.0.0.1", "vagrant", "vagrant")
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
def validation():
    click.secho("Retrieving Information")
    fact = json.dumps(device.get_validation(), sort_keys=True, indent=4)
    click.echo(fact)

@click.command()
def interfaces():
    click.secho("Retrieving Information")
    interface = json.dumps(device.get_interfaces(), sort_keys=True, indent=4)
    click.echo(interface)

@click.command()
def interfaces_ip():
    click.secho("Retrieving Information")
    interface_ip = json.dumps(device.get_interfaces_ip(), sort_keys=True, indent=4)
    click.echo(interface_ip)

@click.command()
def merge():
    click.secho("Merge Loopback Interfaces")
    merge_loopbacks = json.dumps(device.merge_loopbacks(), sort_keys=True, indent=4)
    click.echo(merge)

@click.command()
def replace():
    click.secho("Replace Loopback Interfaces")
    replace_loopbacks = json.dumps(device.replace_loopbacks(), sort_keys=True, indent=4)
    click.echo(replace)

@click.command()
def rollback():
    click.secho("Rollback Loopback Interfaces")
    replace_loopbacks = json.dumps(device.rollback_loopbacks(), sort_keys=True, indent=4)
    click.echo(rollback)

cli.add_command(facts)
cli.add_command(validation)
cli.add_command(interfaces)
cli.add_command(interfaces_ip)
cli.add_command(merge)
cli.add_command(replace)
cli.add_command(rollback)

if __name__ == "__main__":
    cli()
