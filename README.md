# Wifi Monitor Script
This was made by a noob for other noobs (or anyone who wants to use it)
All it does is puts a wireless wifi interface into monitor mode using iw commands.

### Usage:

Install requirements
>pip3 install -r requirements.txt

Enable monitor mode:
> python3 wlan-monitor.py enable -i {interface}

Disable monitor mode
> python3 wlan-monitor.py disable -i {interface}
