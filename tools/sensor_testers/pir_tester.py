#!/usr/bin/env python3
# Digital Device - v20220902.1
# Copyright 2022 - Francesco Ares Sodano

from gpiozero import MotionSensor
from datetime import datetime
from time import sleep

def main():
    try:
        # Initializing Motion PIR
        devicePIR = MotionSensor(4,queue_len=10,sample_rate=10,threshold=0.95)
        print("Motion PIR initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Sensors Initialization error"}
        # Motion PIR error in intialization
        print ("Sensors Initialization error")
        return result
    # Motion detect Loop
    while True:
        devicePIR.wait_for_active()
        sleep(2)
        while devicePIR.is_active:
            # Take the time of detection
            timeNow = datetime.utcnow()
            # Print the detection message
            print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - PIR Activated!")
            sleep(2)          
if __name__ == "__main__": main()