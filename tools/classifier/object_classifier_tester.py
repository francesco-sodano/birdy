#!/usr/bin/env python3
# Object Classifier Tester Tool - v20220902.1
# Copyright 2022 - Francesco Ares Sodano

#import cv2
from curses.textpad import rectangle
from inspect import classify_class_attrs
from types import ClassMethodDescriptorType
from unittest import result
import numpy as np
from PIL import Image, ImageDraw
from tflite_runtime.interpreter import Interpreter

# Configurations
modelLabels = "birdy_efficientdet_lite2_index.txt"
modelTensorflow = "birdy_efficientdet_lite2.tflite"
testImage = "common_chaffinch_2.jpg"
probabilityThreshold = 0.7

def loadModellabels():
    # Load labels for the model
    with open(modelLabels, 'r') as f:
        return {i: line.strip() for i, line in enumerate(f.readlines())}

interpreter = Interpreter(modelTensorflow)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

# Load Model Labels
labels = loadModellabels()

# TensorFlow Model works with 448x448 image size, resizing the original image to match.
image = Image.open(testImage)
image_height, image_width = image.size[:2]
resizedimage=image.resize((input_width, input_height))

#
input_data = np.expand_dims(resizedimage, axis=0)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Retrieve detection results
boxes = interpreter.get_tensor(output_details[0]['index'])[0]
classes = interpreter.get_tensor(output_details[1]['index'])[0]
scores = interpreter.get_tensor(output_details[2]['index'])[0]

results= zip(scores, boxes, classes)

with Image.open(testImage) as im:
    draw = ImageDraw.Draw(im)

# Showing results
for score, box, objDetected in results:
    if score < probabilityThreshold:
        continue
    min_y = round(box[0] * image_height)
    min_x = round(box[1] * image_width)
    max_y = round(box[2] * image_height)
    max_x = round(box[3] * image_width)
    print (f"{labels[int(objDetected)]}: {score*100:.2f}% - {min_x}:{min_y} - {max_x}:{max_y}")
    draw.rectangle([min_x,min_y,max_x,max_y],None,128,2)

im.save("testrectangle.jpg")