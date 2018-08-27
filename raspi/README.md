## Setting up
These instructions are for installing Raspbian with a desktop environment using a Windows PC. After the code has been finalized we may want to install the headless Raspbian Lite to reduce [electricity consumption](https://raspberrypi.stackexchange.com/a/39933).

**Installing Raspbian**
1. Follow the instructions on the official website to [download and flash Raspbian](https://www.raspberrypi.org/documentation/installation/installing-images/) on an SD card.

**Enabling SSH**

2. Add a file called `ssh` to the boot directory of the SD card.

**Connecting to the NUS Wifi**

3. If you have an external monitor and keyboard, go to step 4. Otherwise, go to step 5.
4. Follow instructions on the [official docs](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started/4). Then go to step 10.
5. Install Bonjour print services for windows for mDNS support. 
6. Using and HDMI cable for external display and a mouse (no keyboard needed), boot the pi. Connect to a mobile hotspot that has no password.
7. Ensure your laptop is also connected to the hotspot. Using Putty, ssh into `pi@raspberrypi.local`, default password `raspberry`.
8. Enter `passwd` to change password to `danceteam2`.
9. Install an on-screen keyboard by entering `sudo apt install matchbox-keyboard`. This will allow you to make small changes without needing to SSH.
10. `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf` to configure a connection to the NUS wifi network. First, follow the instructions here to [hash your password](https://unix.stackexchange.com/questions/447979/tu-berlin-eduroam-how-to-get-wireless-lan-working-with-wpa-supplicant-conf-and). Then use the following as a template:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=SG

network={
        ssid="NUS_STU_2-4GHz"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="nusstu\e0001111"
        password=hash:your-hashed-password
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
        priority=1
}
```
11. Follow [these instructions](https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address/74428#74428) to set up a static IP address with dhcpcd.
Note that for a headless install you can create a `wpa_supplicant.conf` file in the boot directory and use the second method in the article above to set up a static IP, possibly bypassing steps 4-9 (untested).
12. Connect to the NUS_STU_2-4GHz network on your PC and ssh into `pi@<static-ip>`. You can now SSH into the pi as long as you are connected to NUS_STU_2-4GHz.

> NOTE: As of 27/08, the raspberry pi loses connection to the internet after about 2 minutes. It remains connected the network but cannot ping the router gateway, other devices on the network, or any website. This occurs with both dynamic and static IPs.
