#!/usr/bin/env python3
# Project Birdy - v202110.1
# Copyright 2021 - Francesco Ares Sodano

import os
import json
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep

def main():
    # Importing settings
    try:
        configFile = './birdy_watcher.conf'
        with open(configFile, "rt") as file:
            deviceConfig = json.load(file)
            print ("File loaded")
    except:
        result = {"statusCode": 400, "statusDescription" : "Error loading configuration"}
        print ("Error loading configuration")
        return result
    # Configuring storage
    try:
        if (os.path.exists('/usr/src/app/birdy_files/')):
            print("Storage attached")
            deviceStorage= '/usr/src/app/birdy_files'
    except:
        result = {"statusCode": 400, "statusDescription" : "Storage not present"}
        print ("Storage not present")
        return result
    # Initializing sensors
    try:
        # Initializing Camera
        deviceCamera = PiCamera()
        deviceCamera.rotation = deviceConfig["device"]["camera"]["rotation"]
        deviceCamera.resolution = (deviceConfig["device"]["camera"]["resolution"]["w"], deviceConfig["device"]["camera"]["resolution"]["h"])
        deviceCamera.framerate = deviceConfig["device"]["camera"]["framerate"]
        deviceCamera.drc_strength = deviceConfig["device"]["camera"]["drc_strength"]
        deviceCamera.exposure_mode = deviceConfig["device"]["camera"]["exposure_mode"]
        # Initializing Motion PIR
        devicePIR = MotionSensor(deviceConfig["device"]["motionpir"]["pin"],queue_len=deviceConfig["device"]["motionpir"]["queue_len"],sample_rate=deviceConfig["device"]["motionpir"]["sample_rate"],threshold=deviceConfig["device"]["motionpir"]["threshold"])
        # Initializing Temperature and Humidity
        # TBD
        print("Sensors initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Sensors Initialization error"}
        print ("Sensors Initialization error")
        return result
    # Motion detect Loop
    while True:
        devicePIR.wait_for_active()
        # wait for the right position of the bird
        sleep(2)
        birdImages = []
        while devicePIR.is_active:
            # take the time of the bird detection
            birdImageTime = datetime.utcnow()
            # take bird picture
            birdImageName = f"{deviceStorage}/images/birdimage{birdImageTime.strftime('%Y%m%d_%H%M%S')}.jpg"
            deviceCamera.capture(birdImageName)        
            birdImages.append(birdImageName)
            print("Image taken")
            sleep(2)
        # prepare the bird file
        birdFileTime = datetime.utcnow()
        birdFileName = f"{deviceStorage}/birdfile{birdFileTime.strftime('%Y%m%d_%H%M%S')}.json"
        birdFile = {
            "date" : birdImageTime.strftime("%d/%m/%Y"),
            "time" : birdImageTime.strftime("%H:%M:%S"),
            "temperature" : 20,
            "humidity" : 45,
            "images" : birdImages
        }
        # write bird file as JSON
        out_file = open(birdFileName,"w")
        json.dump(birdFile,out_file, indent = 4)
        out_file.close()
        # waiting time to reduce false positive
        sleep(5)
        #devicePIR.wait_for_inactive()
        # wait for the inactive queue to be empty
        #sleep(2)
        print("Bird captured")
if __name__ == "__main__": main()