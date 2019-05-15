import napalm
import click
import json

class iosxenapalmapi(object):
    def __init__(self, hostname=None, username=None, password=None, optional_args=None):
        driver = napalm.get_network_driver('ios-xr')
        self.connection = driver(hostname=hostname, username=username, password=password, optional_args={'port':2221})


    def connect(self):
        self.connection.open()

    def disconnect(self):
        self.connection.close()

    def get_facts(self):
        self.connect()
        facts = self.connection.get_facts()
        self.disconnect()
        return facts

    def get_interfaces(self):
        self.connect()
        facts = self.connection.get_interfaces()
        self.disconnect()
        return facts

    def merge_loopbacks(self):
        self.connect()
        facts = self.connection.load_merge_candidate(filename='new_loopbacks.cfg')
        print('\nDiff:')
        print(self.connection.compare_config())
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
        print(self.connection.compare_config())
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


    def rollback_loopbacks(self):
        self.connect()
        facts = self.connection.load_merge_candidate(filename='new_loopbacks.cfg')
        print('\nDiff:')
        print(self.connection.compare_config())
        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        except NameError:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == 'y':
            print('Committing ...')
            self.connection.commit_config()

        elif choice == 'N':
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()

        rollback = input("\nWould you like to rollback these changes? [yN]: ")
        if choice == 'y':
            print('Reverting ...')
            self.connection.rollback()

        if choice == 'N':
            print('Discarding ...')
            self.connection.discard_config()
            self.disconnect()


device = iosxenapalmapi("127.0.0.1", "vagrant", "vagrant")

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
cli.add_command(interfaces)
cli.add_command(merge)
cli.add_command(replace)
cli.add_command(rollback)

if __name__ == "__main__":
    cli()
