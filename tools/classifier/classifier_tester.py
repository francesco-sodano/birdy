#!/usr/bin/env python3
# Classifier Tester Tool - v20220902.1
# Copyright 2022 - Francesco Ares Sodano

from datetime import datetime
import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter
import json

# Configurations
modelLabels = "birdy16_index.txt"
modelTensorflow = "birdy16.tflite"
testImage = "common_chaffinch_2.jpg"
probabilityThreshold = 0.6

def loadModellabels():
    # Load labels for the model
    with open(modelLabels, 'r') as f:
        return {i: line.strip() for i, line in enumerate(f.readlines())}

def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

def classifyImage(interpreter, image, top_k=1):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))

    # if model is quantized (uint8 data), then dequantize the results
    if output_details['dtype'] == np.uint8:
        scale, zero_point = output_details['quantization']
        output = scale * (output - zero_point)

    ordered = np.argpartition(-output, top_k)
    return [(i, output[i]) for i in ordered[:top_k]]

def identifyBird():
    """ is there a bird at the feeder? """
    image = Image.open(testImage)
    resizedImage=image.resize((112,112))
    resizedImage.save("resizeimage.jpg")
    labels = loadModellabels()
    interpreter = Interpreter(modelTensorflow)
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']
    results = classifyImage(interpreter, resizedImage)
    label_id, prob = results[0]
    print("bird: " + labels[label_id])
    print("prob: " + str(prob))
    
    if prob > probabilityThreshold:
        bird = labels[label_id]
        bird = bird[bird.find(",") + 1:]
        prob_pct = str(round(prob * 100, 1)) + "%"
        print(bird, prob_pct)

def main():
    identifyBird()
if __name__ == "__main__": main()

