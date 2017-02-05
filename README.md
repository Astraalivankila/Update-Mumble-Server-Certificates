# Update Mumble Server Certificates
A script for updating SSL key and certificate on the fly with no reboot for Mumble server. Specificially designed for Lets Encrypt certificate auto renewal.

Depends on [Mice](https://wiki.mumble.info/wiki/Mice) and Python.

###**PLEASE NOTE: REQUIRES MUMBLE SERVER >1.3.**

## Usage

1. Make sure your Mumble server has [Ice enabled](https://wiki.mumble.info/wiki/Ice#Getting_ready_to_use_Ice).
2. Download the [latest version](https://github.com/mumble-voip/mumble-scripts/blob/master/Helpers/mice.py) of Mice and set it up. Remember to change ice secrets, hosts and ports.
3. Place **certupdate.py** to the same folder with Mice. Edit the configuration to match your setup.
4. Run the script. 
5. Alternatively, automate it with a shell script and cron. (Example script coming soon)
