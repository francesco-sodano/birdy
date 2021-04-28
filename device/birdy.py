#!/usr/bin/env python3
# Digital Device - v20210330.1
# Copyright 2021 - Francesco Ares Sodano

import os
import asyncio
from pijuice import PiJuice
from gpiozero import MotionSensor, CPUTemperature
from picamera import PiCamera
from datetime import datetime
from getmac import get_mac_address
from retrying import retry 
from time import sleep
from azure.iot.device.aio import IoTHubDeviceClient, IoTHubModuleClient
from azure.iot.device import Message
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import AzureError, ResourceExistsError


class birdy:
    def __init__(self, iotDeviceConnectionString, deviceStorage, devicePosition = "('51.477878','-0.001267')"):
        """
        Create the digital version of the Birdy device

        iotDeviceConnectionString (str) - Device connection string for Azure IoT Hub
        deviceStorage (str) - Path to temporary store bird picture before Azrue upload and logs
        devicePosition (tuple) - GPS coordinates where Birdy device is positioned 
        """
        # Device Information
        self._deviceID =  get_mac_address(interface="wlan0")
        self._deviceName = os.uname()[1]
        self._devicePosition = devicePosition
        self._deviceVersion = os.getenv("birdDetectionVersion")
        self._deviceConnectionString = iotDeviceConnectionString
        self._deviceIsConnected = False
        # Device Tools Initialization
        self._deviceHat = PiJuice(1, 0x14)
        self._devicePIR = MotionSensor(4,queue_len=2,sample_rate=10,threshold=0.9)
        self._deviceCamera = PiCamera()
        # Device Camera Settings
        self._deviceCamera.rotation = 180
        self._deviceCamera.resolution = (2592, 1944)
        self._deviceCamera.framerate = 15
        self._deviceCamera.drc_strength = 'low'
        self._deviceCamera.exposure_mode = 'auto'
        # Device Initialization
        self._deviceStorage = deviceStorage
        self._deviceClient = IoTHubDeviceClient.create_from_connection_string(iotDeviceConnectionString)

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_delay=30000)
    async def deviceConnect(self):
        try:
            await self._deviceClient.connect()
            self._deviceIsConnected = True
            return True
        except AzureError as ex:
            # catch Azure errors that might result from Init operation
            self._deviceIsConnected = False
            raise Exception("not connected")
            return False

    def deviceStatus(self):
        """
        Returns device status
        """
        return('{' + f'"Device Name" : "{self._deviceName}", \
            "Device ID" : "{self._deviceID}", \
            "GPS Location" : {self._devicePosition}, \
            "Connected" : {self._deviceIsConnected}, \
            "Device Temp" :  {CPUTemperature().temperature}, \
            "Battery Level" : {self._deviceHat.status.GetChargeLevel()["data"]}, \
            "Battery Voltage" : {self._deviceHat.status.GetBatteryVoltage()["data"]}, \
            "Battery Ampere" : {self._deviceHat.status.GetBatteryCurrent()["data"]}, \
            "Power Input Voltage" : {self._deviceHat.status.GetIoVoltage()["data"]}, \
            "Power Input Ampere" : {self._deviceHat.status.GetIoCurrent()["data"]}' + '}')

    def deviceSetPowerSettings(self):
        print("TO DO")
    
    def deviceGetPowerSettings(self):
        print("TO DO")

    def deviceSetLocation(self, devicePosition):
        print("TO DO")
    
    def deviceGetLocation(self):
        print("TO DO")

    def deviceSetCameraSettings(self):
        print("TO DO")

    def deviceGetCameraSettings(self):
        print("TO DO")

    async def birdDetect(self):
        """
        Takes picture of the bird as soon as the PIR is activated.
        """
        self._devicePIR.wait_for_active()
        birdImageTime = datetime.utcnow()
        birdImage = f"{self._deviceStorage}/birdImage{birdImageTime.strftime('%Y%m%d_%H%M%S')}.jpg"
        self._deviceCamera.capture(birdImage)
        try:
            await self.__birdUpload(birdImage, birdImageTime)
            sleep(2)
            self._devicePIR.wait_for_inactive()
            result = {"statusCode": 200, "statusDescription" : birdImage}
            sleep(1)
        except:
            result = {"statusCode": 401, "statusDescription" : "Image Upload Error"}
        return result

    async def __birdUpload(self, birdImage, birdImageTime):
        birdImageName = birdImage.rsplit('/',1)[1]
        try:
            storageInfo = await self._deviceClient.get_storage_info_for_blob(birdImageName)
            blobUri = f'https://{storageInfo["hostName"]}/{storageInfo["containerName"]}/{storageInfo["blobName"]}{storageInfo["sasToken"]}'
            blobClient = BlobClient.from_blob_url(blobUri)
            with open(birdImage,"rb") as data:
                blobClient.upload_blob(data)
            messageData = '{' + f'"deviceName" : "{self._deviceName}", \
            "deviceID" : "{self._deviceID}", \
            "gpsLocation" : {self._devicePosition}, \
            "blobUri" : {blobUri}, \
            "captureTime" : {birdImageTime}' + '}'
            message = Message(messageData)
            message.custom_properties["messageType"] = "birdDetect"
            await self._deviceClient.send_message(message)
            result = {"statusCode": 200, "statusDescription" : messageData}
            #os.remove(birdImage)
            blobClient.close()
        except:
            result = {"statusCode": 400, "statusDescription" : "Storage Blob Upload Error"}
        return result

    async def deviceRetrieveTwin(self):
        """
        Gets the device or module twin from the Azure IoT Hub service.
        This is a synchronous call, meaning that this function will not return until the twin has been retrieved from the service.
        """
        _deviceTwin = await self._deviceClient.get_twin()
        return _deviceTwin

    async def deviceReportTwin(self):
        """
        Update reported properties with the Azure IoT Hub service.
        This is a synchronous call, meaning that this function will not return until the patch has been sent to the service and acknowledged.
        If the service returns an error on the patch operation, this function will raise the appropriate error.
        """
        # batterylevel = self._deviceHat.status.GetChargeLevel()["data"]
        _reportedProperties = {'deviceID' : f'{self._deviceID}', \
            'gpsLocation' : f'{self._devicePosition}', \
            'batteryLevel' : f'{self._deviceHat.status.GetChargeLevel()["data"]}', \
            'deviceTemp' : f'{CPUTemperature().temperature}', \
            'batteryVolt' : f'{self._deviceHat.status.GetBatteryVoltage()["data"]}', \
            'batteryAmpere' : f'{self._deviceHat.status.GetBatteryCurrent()["data"]}', \
            'powerInputVolt' : f'{self._deviceHat.status.GetIoVoltage()["data"]}', \
            'powerInputAmpere' : f'{self._deviceHat.status.GetIoCurrent()["data"]}'}
        await self._deviceClient.patch_twin_reported_properties(_reportedProperties)

    async def deviceSendTelemetry(self):
        messageData = self.deviceStatus()
        message = Message(messageData)
        message.custom_properties["messageType"] = "deviceStatus"
        await self._deviceClient.send_message(message)
        return (message)

#----------------------------------------------------------------------------------------------------------------------

async def main():
    imagedir = f'{os.getcwd()}/images'
    connectionString = os.getenv("iotDeviceConnectionString")
    device = birdy(connectionString, imagedir)
    await device.deviceConnect()
    while True:
        await device.birdDetect()
    

if __name__ == "__main__": asyncio.run(main())