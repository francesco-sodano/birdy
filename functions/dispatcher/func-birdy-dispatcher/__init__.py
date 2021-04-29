#!/usr/bin/env python3
# Azure Function for Image - v20210317.1
# Copyright 2021 - Francesco Ares Sodano

# Import libraries
from typing import List
import logging
import json
import os
import azure.functions as func

def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info('Function Started!')
        data = event.get_body().decode('utf-8')
        properties = event.metadata['PropertiesArray'][0]
        logging.info(properties['messageType'])
        logging.info(str(data))
            #image_metadata = json.loads(data)
            #success = image_metadata['success']
            #blobUri = image_metadata['blobUri']
            #filename = image_metadata['filename']
            #deletelocal = image_metadata['deletelocal']
            #logging.info(f'File uploaded: {blobUri}')
            #logging.info(f'Name of the file: {filename}')