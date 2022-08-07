#!/usr/bin/env python3
# Project Birdy - v202110.1
# Copyright 2021 - Francesco Ares Sodano

import os
import json
from pijuice import PiJuice
from gpiozero import CPUTemperature
from datetime import datetime
from time import sleep
from azure.iot.device.aio import IoTHubDeviceClient, IoTHubModuleClient
from azure.iot.device import Message
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import AzureError, ResourceExistsError

def main():
    # Importing settings
    try:
        configFile = f'{os.path.dirname(os.getcwd())}/birdy_config.json'
        with open(configFile, "rt") as file:
            deviceConfig = json.load(file)
            print ("File loaded")
    except:
        result = {"statusCode": 400, "statusDescription" : "Error loading configuration"}
        print ("Error loading configuration")
        return result
    # Open Connection

    # Get list of all bird files in the folder

    # For each bird file

        # Enrich file

        # Upload Images

        # Send message

        # Clean bird file and images
     
    # Close Connection       

if __name__ == "__main__": main()   