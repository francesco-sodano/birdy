#!/usr/bin/env python3
# Azure Function for Image - v20210317.1
# Copyright 2021 - Francesco Ares Sodano

# Import libraries
import logging
import json
import os
import azure.functions as func
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from typing import List

def main(events: List[func.EventHubEvent]):
    cogCredentialKey = os.environ['ComputerVisionKey']
    cogEndpoint = os.environ['ComputerVisionEndpoint']
    imageFeature = ["categories"]
    storageAccountUploadConnectionString = os.environ['StorageAccountUploadConnectionString']
    try:
        for event in events:
            logging.info('Function Started!')
            data = event.get_body().decode('utf-8')
            properties = event.metadata['PropertiesArray'][0]
            messageData = json.loads(data)
            # Telemetry message
            if properties['messageType'] == 'deviceStatus':
                logging.info(properties['messageType'])
                logging.info(str(data))
            # Bird detected message
            elif properties['messageType'] == 'birdDetect':
                cogCredential = CognitiveServicesCredentials(cogCredentialKey)
                cogClient = ComputerVisionClient(endpoint=cogEndpoint,credentials=cogCredential)
                blobService = BlobClient.from_connection_string(conn_str=storageAccountUploadConnectionString, container_name=messageData['containerName'], blob_name=messageData['blobName'])
                blobImage = BlobClient.download_blob()
                imageCategories = cogClient.analyze_image_in_stream(blobImage,imageFeature)
                if (len(imageCategories) == 0):
                    logging.warning("No categories detected")
                else:
                    for category in imageCategories:
                        if (category.name == 'animal_bird') and (category.score > 0.75):
                            logging.info("bird detected")
                            print("TO DO")
                        else:
                            logging.warning("Not a bird")
                            print("TO DO")
            
            #messageData = '{' + f'"deviceName" : "{self._deviceName}", \
            #"deviceID" : "{self._deviceID}", \
            #"gpsLocation" : {self._devicePosition}, \
            #"containerName" : {storageInfo["containerName"]}, \
            #"blobname" : {storageInfo["blobName"]}, \
            #"captureTime" : {birdImageTime}' + '}'
            # should be a function in the module later
            else:
                logging.info(properties['messageType'])
    except:
        logging.error("it exploded!")

