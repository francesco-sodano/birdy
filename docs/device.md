# The Device

The device is composed by hardware and software components.

There are different versions and variants of the device in this repository.

the macro-components of the device are the following:

1. Bird Feeder
2. Smart Box
3. Roof Top

## Bird Feeder

The Bird feeder is the main 3D Printed component of the device. it has the function of storing and deploy seeds and to handle the any version of the Smart box.

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/device/birdy_feeder_nosmartbox.jpg" width= 50%>
</p>

the Smart Box is detachable without compromise basic function of the feeder: it means you can use Birdy as standard feeder without the smart box.

## Smart Box

The Smart Box contians all the sensors, the battery and the compute for birdy.
It's easely detachable so you can bring it with you, leaving the feeder in its position.

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/device/birdy_smartbox_closed.jpg" width= 50%>
</p>

The SmartBox is designed to work with a PiJuice Hat that works as power controller and can be configured and managed remotely: for example you can configure the smartbox to shutdown in the night and turn on again at dawn or shutdown when the battery power is at certain battery level and turn it on again when the solar panel rechanged the battery.

The Smart Box has two different versions:

1. **DEV Version**: this is based on Raspberry Pi 3 B+ and it's used for development. Raspberry Pi 3 B+ is able to handle direct connetion with Visual Studio Code for debugging. the battery life it's ok for few hours sessions.

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/device/birdy_smartbox_dev_open.jpg" width= 50%>
</p>

2. **PROD Version**: this is based on Raspberry Pi Zero W and it's used for production. it's requires less power and has a better battery life to permit long sessions (up to one week).

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/device/birdy_smartbox_prod_open.jpg" width= 50%>
</p>

The Smart box could be also directly connected to a power supply so Birdy can be always up and running.

## Roof Top

The Roof Top has also two different variants:

1. **Standard**: this is standard 3D printed roof.

2. **Solar Powered**: this is an enhanched version that includes a solar panel able to rechanrge the battery of the Smart Box and increase the autonomy of the device.

# Hardware Components

the **DEV Version** of the device requires the following hardware:

1. [Raspberry Pi 3 model B+](https://uk.pi-supply.com/products/raspberry-pi-3-model-b-plus?_pos=64&_sid=6161a3a4c&_ss=r1)
2. [Grove mini PIR motion sensor](https://www.seeedstudio.com/Grove-mini-PIR-motion-sensor-p-2930.html)
3. [Raspberry Pi camera board v2.1](https://uk.pi-supply.com/products/raspberry-pi-camera-board-v2-1-8mp-1080p?_pos=48&_sid=6161a3a4c&_ss=r)
4. [Raspberry Pi camera lens 160 degree](https://uk.pi-supply.com/products/camera-module-for-official-raspberry-pi-camera-board-v2-8mp-sensor-160-degree)
5. [PiJuice Standard with 1820mAh battery](https://uk.pi-supply.com/products/pijuice-standard)

the **PROD Version** of the device requires the following hardware:

1. [Raspberry Pi Zero W (with soldered header)](https://uk.pi-supply.com/products/raspberry-pi-zero-w-soldered-header)
2. [Grove mini PIR motion sensor](https://www.seeedstudio.com/Grove-mini-PIR-motion-sensor-p-2930.html)
3. [Raspberry Pi camera board v2.1](https://uk.pi-supply.com/products/raspberry-pi-camera-board-v2-1-8mp-1080p?_pos=48&_sid=6161a3a4c&_ss=r)
4. [Raspberry Pi camera lens 160 degree](https://uk.pi-supply.com/products/camera-module-for-official-raspberry-pi-camera-board-v2-8mp-sensor-160-degree)
5. [PiJuice Zero](https://uk.pi-supply.com/products/pijuice-zero?_pos=1&_sid=bd8682207&_ss=r)
6. [PiJuice Zero 1200mAh battery](https://uk.pi-supply.com/products/pijuice-zero-1200mah-battery?_pos=2&_sid=d94484a36&_ss=r)

The **Solar Version** of the device requires this additional hardware

1. [Solar Panel GH165x135 3.5W 6V USB](https://www.fruugoschweiz.com/35w-usb-solar-panel-digital-ladegerat-fur-mobile/p-88157157-183939064?language=de&ac=bing&msclkid=8a319213ee5a1f8c2379f0fd8141d564&utm_source=bing&utm_medium=cpc&utm_campaign=All_190785_CH&utm_term=4575274048654658&utm_content=Ad%20group%20%231)
# Component Matrix


