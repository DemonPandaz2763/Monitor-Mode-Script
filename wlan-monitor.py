import click
import subprocess
import pyfiglet

@click.group()
def my_cmds():
    pass

@click.command(help="Enable monitor mode on interface")
@click.option("-i", "--interface", prompt="Select interface", help="Select your interface.")
def enable(interface):

    ascii_banner = pyfiglet.figlet_format("ENABLING INTERFACE")
    print(ascii_banner)
    
    try:
        subprocess.run(['sudo', 'ifconfig', interface, 'down'], check=True)
        print(f"Disabled interface {interface}. -_-")
        subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'monitor'], check=True)
        print(f"Enabled monitor mode on {interface}. -_-")
        subprocess.run(['sudo', 'ifconfig', interface, 'up'], check=True)
        print(f"Enabled interface {interface}. -_-")
        print(f"Network interface {interface} is now ready to use. :D")
    except subprocess.CalledProcessError as e:
        print(f"Error: Something fucked up. Good luck. XD")

@click.command(help="Disable monitor mode on interface")
@click.option("-i", "--interface", prompt="Select interface", help="Select your interface.")
def disable(interface):

    ascii_banner = pyfiglet.figlet_format("DISABLING INTERFACE")
    print(ascii_banner)
    
    try:
        subprocess.run(['sudo', 'ifconfig', interface, 'down'], check=True)
        print(f"Disabled interface {interface}. -_-")
        subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'managed'], check=True)
        print(f"Disabled monitor mode on {interface}. -_-")
        subprocess.run(['sudo', 'ifconfig', interface, 'up'], check=True)
        print(f"Enabled interface {interface}. -_-")
        print(f"Network interface {interface} is now ready to use. :D")
    except subprocess.CalledProcessError as e:
        print(f"Error: Something fucked up. Good luck. XD")

my_cmds.add_command(enable)
my_cmds.add_command(disable)

if __name__ == "__main__":
    my_cmds()
