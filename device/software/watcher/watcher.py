#!/usr/bin/env python3
# Project Birdy - v202110.1
# Copyright 2021 - Francesco Ares Sodano

import os
import sys
import asyncio
import json
from gpiozero import MotionSensor, CPUTemperature
from picamera import PiCamera
from datetime import datetime
from getmac import get_mac_address
from time import sleep

def main():
    # Importing settings
    try:
        configFile = f'{os.path.dirname(os.getcwd())}/config/birdy-config.json'
        with open(configFile, "rt") as file:
            configuration = json.load(file)
    except:
        result = {"statusCode": 400, "statusDescription" : "Error loading configuration"}
        return result
        sys.exit(1)
    # Configuring storage
    
    # Initializing sensors
    
    # Motion detect Loop

    print("TBD")
    result = {"statusCode": 200, "statusDescription" : "Program completed"}
    return result
if __name__ == "__main__": main()
