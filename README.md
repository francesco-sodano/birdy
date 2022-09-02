
<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/birdy-logo.jpg" width= 60%>
</p>

# Birdy - The Open-Source Smart Feeder to fight climate change
Birdy is a nicely designed wild bird feeder that takes photos, identifies and classifies birds. - based on Raspberry Pi, Azure IoT Edge and Azure Cognitive Service.

# Inspiration

Let's play a game! :)

***Question 1: Did you know that in many countries birdwatching is more popular than gardening?***

However, as you can't just sit around your bird feeder all the time, you miss out on a lot of action.

***Question 2: Did you know that birds play several essential and indispensable roles in the ecosystems they reside in and travel through?***

Birds raising broods end up acting as pest control agents by devouring insects and other organisms that harm the environment and crops. Migratory birds help in dispersal of seeds, leading to maintenance of biodiversity along their routes.

***Question 3: Did you know that bird feeders are helping migrating birds?***

Climate change does a lot more than just heat up our planet. Climate change can also cause more intense weather. That could mean more hurricanes, floods, heat waves, droughts, and even cold spells.
This extreme weather can be trouble for birds. Scientists have noticed that when extreme weather happens, fewer birds show up in the places they call home.
If birds are moving to other areas because of climate change, they may need our help and we may need to protect their new habitats.
Having bird feeders along their route will help to keep migrating birds energized to complete their journey forward. In months like the winter, bird feeders act almost like an oasis of food for these feathery creatures.

So what if will be able to combine all these in one single, open solution that:

1. Helps to identify, classify and register birds that are coming to visit our houses 
2. Shares those data worldwide, to identify new or established migration routes and define new natural reserves to fight the climate change
3. Works on our side to NOT miss out any visit you are having in your garden

these are the reasons why we created **Project Birdy**

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/misc/birdy-device-promopicture1.jpg" width= 60%>
</p>

# The Project Repository

the repository is organized in this way:

1. *backend*: contains the contains the IaC for the backend deployment and the source code for the backend running on the infrastructure created.
2. *device*: contains the device STL for 3d printing and the software to run on the device.
3. *docs*: contains the step-by-step documentation for put in place the entire solution
4. *mobile*: contains the source code for the mobile app
5. *res*: contains static resources like images to be used in the doc files
6. *tools*: contains any additional resource you may need to put in place the solution

# The Device

The device is based on Raspberry Pi and use Azure IoT Edge framework.

<p align="center">
<img src="https://github.com/francesco-sodano/birdy/raw/main/res/images/doc/doc-device-architecture.png" width= 60%>
</p>

More info can be found here: [The Device](https://github.com/francesco-sodano/birdy/blob/main/docs/device.md)

# The Back-end



# The Mobile App

# Notice

1. **Privacy** is always important for us. Birdy is designed and configured to have a very short focus range (5 cm max). it means that everything out of this range will be out-of-focus and blurred.
2. **Squirrels** are usually a common issues for bird feeders: There is actually no way to stop squirrels to come to the feeder but hey.. let's them eat too.. we are nature friends! :). Birdy as anyway a specific function to detect squirrel presence and don't collect pictures (also with an alert for the Birdy owner if configured).

# Table of Content

1. [Read Me](https://github.com/francesco-sodano/birdy/blob/main/README.md)
2. [The Device](https://github.com/francesco-sodano/birdy/blob/main/docs/device.md)
3. [Architecture](https://github.com/francesco-sodano/birdy/blob/main/docs/architecture.md)
4. [Deployment](https://github.com/francesco-sodano/birdy/blob/main/docs/deployment.md)
5. [Setup](https://github.com/francesco-sodano/birdy/blob/main/docs/instructions.md)