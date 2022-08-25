# Setup Birdy

# Prepare Raspberry Pi

Raspberry Pi recommend the use of Raspberry Pi Imager to install an operating system on to your SD card. You will need another computer with an SD card reader to install the image.
The image required is 

## Enable ssh

In the boot volume, create a file without an extension and name it "ssh"

## Include Wi-Fi

In the boot volume, create a file called "wpa_supplicant.conf"

```python
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CH
network={
    ssid="WIFI_SSID"
    scan_ssid=1
    psk="WIFI_PASSWORD"
    priority=1
    key_mgmt=WPA-PSK
}
```
## Setup 
Setup Raspberry: https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

Secure Raspberry: https://www.raspberrypi.com/documentation/computers/configuration.html#securing-your-raspberry-pi

Passwordless access: https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md#copy-your-public-key-to-your-raspberry-pi

## Install required Packages:

sudo apt update
sudo apt install git pijuice-base python3-pip python3-gpiozero
sudo apt install pip3 debugpy gpiozero picamera azure-eventhub azure-iot-device azure.storage.blob get-mac retrying

## Configure raspi-config

Configurations (with raspi-config):
 - Enable Camera
 - Enable I2C
 - Add Timezone


## Configure Camera settings

Modfiy the following line in the "Automatically load overlays for detected cameras"

```python
camera_auto_detect=0
```

Add this line to the "Enable DRM VC4 V3D driver" section

```python
dtoverlay=imx219,mediacontroller=0
max_framebuffers=2
```


Add the follwoing lines at the end of the "/boot/config.txt" file

```python
gpu_mem=32
start_file=start_x.elf
fixup_file=fixup_x.dat
```

## Setting the RTC (PiJuice)

After setting the date and time you must then copy the system time to the RTC with the command:

sudo hwclock -w

You can check this with:

sudo hwclock -r

When the Raspberry Pi shutsdown and then reboots you must copy the RTC time back to the system clock at boot and you can do this in /etc/rc.local (using sudo vi) with 

sudo hwclock -s.

# Device Optimization

## Disable Bluetooth

Edit /boot/config.txt and add the following line at the bottom:
    dtoverlay=pi3-disable-bt
then run:
    sudo systemctl disable bluetooth.service
on the next boot you can run the following command to check that BT is disabled:
hcitool dev

## Disable HDMI

Add the line to /etc/rc.local to disable HDMI on boot. 
/usr/bin/tvservice -o

## Disable USB Chip

echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind

## Add Environment variable

Create a new file under /etc/profile.d to store the global environment variable(s). The name of the should be contextual so others may understand its purpose (for explample birddetector.sh)

sudo touch /etc/profile.d/birdy.sh
sudo vi /etc/profile.d/birdy.sh

add the following line in vi.

export iotDeviceConnectionString="VALUE"
export birdDetectionVersion="20200330-1.0"

# Trainer

pip install azure-cognitiveservices-vision-customvision


# Functions
pip install azure-storage-blob
pip install azure-cognitiveservices-vision-computervision