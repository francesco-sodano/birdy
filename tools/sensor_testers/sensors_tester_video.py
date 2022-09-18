from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from datetime import datetime
from gpiozero import MotionSensor
from time import sleep

def main():
    try:
        # Initializing Motion PIR
        devicePIR = MotionSensor(4,queue_len=5,sample_rate=10,threshold=0.99)
        print("Motion PIR initialized")
    except:
        result = {"statusCode": 400, "statusDescription" : "Motion PIR Initialization error"}
        # Motion PIR error in initialization
        print ("Motion PIR Initialization error")
        return result
    try:
        # Initializing Camera
        tuning = Picamera2.load_tuning_file("imx219.json")
        deviceCamera = Picamera2(tuning=tuning)
        deviceCameraConfig = deviceCamera.create_video_configuration(main={"size": (1920, 1080)})
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
                # Taking Video
                print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - Taking Video!")
                encoder = H264Encoder(bitrate=10000000)
                output = FfmpegOutput(f"video-{timeNow.strftime('%Y%m%d_%H%M%S')}.mp4")
                deviceCamera.start_recording(encoder, output)
                sleep(10)
                devicePIR.wait_for_inactive()
                deviceCamera.stop_recording()
                print(f"{timeNow.strftime('%Y%m%d_%H%M%S')} - All Done!")
                sleep(2)
            except:
                result = {"statusCode": 400, "statusDescription" : "Camera issue on taking video"}
                # Camera error in taking picture
                print ("Camera issue on taking video")
                return result                
if __name__ == "__main__": main()