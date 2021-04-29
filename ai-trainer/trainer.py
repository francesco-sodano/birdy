#!/usr/bin/env python3
# Digital Device - v20210330.1
# Copyright 2021 - Francesco Ares Sodano

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

cv_endpoint = "<INSERT CUSTOM VISION ENDPOINT>"
training_key = "<INSERT TRAINING KEY>"
training_images = "<LOCATION FOR THE TRAINING IMAGES>"

# Create a training client
trainer = CustomVisionTrainingClient(training_key, endpoint= cv_endpoint)

# List all available domains
for domain in trainer.get_domains():
  print(domain.id, "\t", domain.name) 

# Create a project
project = trainer.create_project("Birdy - v1","0732100f-1a38-4e49-a514-c9b44c697ab5")

# Create the tags and add the images to a list
image_list = []
directories = os.listdir(training_images)

for tagName in directories:
 	tag = trainer.create_tag(project.id, tagName)
 	images = os.listdir(os.path.join(training_images,tagName))
 	for img in images:
 		with open(os.path.join(training_images,tagName,img), "rb") as image_contents:
 			image_list.append(ImageFileCreateEntry(name=img, contents=image_contents.read(), tag_ids=[tag.id]))  

# Create chunks of 64 images
def chunks(l, n):
 	for i in range(0, len(l), n):
 		yield l[i:i + n]
batchedImages = chunks(image_list, 64)

# Upload the images in batches of 64 to the Custom Vision Service
for batchOfImages in batchedImages:
 	upload_result = trainer.create_images_from_files(project.id, images=batchOfImages)
  
# Train the model
import time
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
 	iteration = trainer.get_iteration(project.id, iteration.id)
 	print ("Training status: " + iteration.status)
 	time.sleep(1)

# Publish the iteration of the model
publish_iteration_name = '<INSERT ITERATION NAME>'
resource_identifier = '<INSERT RESOURCE IDENTIFIER>'
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, resource_identifier)
