#!/usr/bin/env python3
# Camera Tester Tool - v20220902.1
# Copyright 2022 - Francesco Ares Sodano

from picamera2 import Picamera2
from datetime import datetime

def main():
    try:
        # Initializing Camera
        deviceCamera = Picamera2()
        deviceCameraConfig = deviceCamera.create_still_configuration()
        deviceCamera.configure(deviceCameraConfig)
        print("Camera initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Sensors Initialization error"}
        # Camera error in initialization
        print ("Sensors Initialization error")
        return result
    try:
        # Taking set of pictures
        deviceCamera.start_and_capture_files("test{:d}.jpeg", initial_delay=0, delay=1, num_files=10, show_preview=False)
    except:
        result = {"statusCode": 400, "statusDescription" : "Camera issue on taking photo"}
        # Camera error in taking picture
        print ("Camera issue on taking photo")
        return result
if __name__ == "__main__": main()