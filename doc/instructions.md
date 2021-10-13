# Setup Birdy

Enable ssh

In the boot volume, create a file without an extension and name it ssh

Include Wi-Fi

https://linuxhint.com/rasperberry_pi_wifi_wpa_supplicant/

wpa_supplicant.conf

country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="WIFI_SSID"
scan_ssid=1
psk="WIFI_PASSWORD"
key_mgmt=WPA-PSK
}

# Raspberry Pi
Setup Raspberry: https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

Secure Raspberry: https://www.raspberrypi.com/documentation/computers/configuration.html#securing-your-raspberry-pi

Passwordless access: https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md#copy-your-public-key-to-your-raspberry-pi

Packages:

sudo apt update

sudo apt install git pijuice-base python3-pip python3-gpiozero

sudo apt install pip3 debugpy gpiozero picamera azure-eventhub azure-iot-device azure.storage.blob get-mac retrying

Configurations (with raspi-config):
 - Enable Camera
 - Enable I2C
 - Add Timezone

Setting the RTC (PiJuice)

After setting the date and time you must then copy the system time to the RTC with the command:

sudo hwclock -w

You can check this with:

sudo hwclock -r

When the Raspberry Pi shutsdown and then reboots you must copy the RTC time back to the system clock at boot and you can do this in /etc/rc.local (using sudo vi) with 

sudo hwclock -s.

# Device Optimization

Disable Bluetooth
Edit /boot/config.txt and add the following line at the bottom:
    dtoverlay=pi3-disable-bt
then run:
    sudo systemctl disable bluetooth.service
on the next boot you can run the following command to check that BT is disabled:
hcitool dev

Disable HDMI
Add the line to /etc/rc.local to disable HDMI on boot. 
/usr/bin/tvservice -o
Reduce memory for video in /boot/config.txt
gpu_mem=16 

Disable USB Chip

echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind

Add Environment virable

Create a new file under /etc/profile.d to store the global environment variable(s). The name of the should be contextual so others may understand its purpose (for explample birddetector.sh)

sudo touch /etc/profile.d/birddetector.sh
sudo vi /etc/profile.d/birddetector.sh

add the following line in vi.

export iotDeviceConnectionString="VALUE"
export birdDetectionVersion="20200330-1.0"

# Trainer

pip install azure-cognitiveservices-vision-customvision


# Functions
pip install azure-storage-blob
pip install azure-cognitiveservices-vision-computervision