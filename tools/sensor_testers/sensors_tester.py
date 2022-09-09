#!/usr/bin/env python3
# Camera Tester Tool - v20220902.1
# Copyright 2022 - Francesco Ares Sodano

from picamera2 import Picamera2
from datetime import datetime
from gpiozero import MotionSensor
from time import sleep

def main():
    try:
        # Initializing Motion PIR
        devicePIR = MotionSensor(4,queue_len=9,sample_rate=3,threshold=0.90)
        print("Motion PIR initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Motion PIR Initialization error"}
        # Motion PIR error in initialization
        print ("Motion PIR Initialization error")
        return result
    try:
        # Initializing Camera
        deviceCamera = Picamera2()
        deviceCameraConfig = deviceCamera.create_still_configuration()
        deviceCamera.configure(deviceCameraConfig)
        print("Camera initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Camera Initialization error"}
        # Camera error in initialization
        print ("Camera Initialization error")
        return result
    # Motion detect Loop
    while True:
        devicePIR.wait_for_active()
        while devicePIR.is_active:
            try:
                # Take the time of detection
                timeNow = datetime.utcnow()
                print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - PIR Activated!")
                # Taking set of pictures
                print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - Taking photos!")
                deviceCamera.start_and_capture_files(f"image-{timeNow.strftime('%Y%m%d_%H%M%S')}""-{:d}.jpeg", initial_delay=0, delay=1, num_files=3, show_preview=False)
                print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - All Done!")
            except:
                result = {"statusCode": 400, "statusDescription" : "Camera issue on taking photo"}
                # Camera error in taking picture
                print ("Camera issue on taking photo")
                return result          
        devicePIR.wait_for_inactive()          
if __name__ == "__main__": main()