# Smart Train
The Smart Train project was created in cooperation between the [University of West Bohemia](https://www.zcu.cz/en/index.html) and the [Church Grammar School in Pilsen](https://cirkevni-gymnazium.cz/).  
![University of West Bohemia](https://www.zcu.cz/en/assets/logo.svg)
## Introduction
During the school year, the students of the Church Grammar School had worked on a model of train that would be exceptional in its abilities. One of the leading features was for it to be controlled by an artificial intelligence that would recognize the lights on the traffic lights and control the train accordingly. Another peculiarity is that it is not a classic train, but a monorail that will balance on the tracks using a gyroscope so that it does not derail.  
![Smart Train Design](/SmartTrain_design.png)
## Our work
In order to increase work efficiency, we divided the individual tasks among ourselves. In the end, however, it turned out that we had to help each other with the individual tasks. 
### Hardware
We decided to power the whole train with a Raspberry Pi. It is a powerful microcomputer, which is additionally enriched with pins, thanks to which other devices such as sensors can be easily connected to. We chose a digital temperature sensor and BNO055 (the gyroscope).
### Software
The artificial intelligence was done using TensorFlow.  
The data from all the sensors are being uploaded to our server (specifically to our InfluxDB database) and then redirected to Grafana which we use to display the output data.  
For the the slicing of our train we used PrusaSlicer.  
We did encounter a lot of difficulties during the making of this project but we did manage to solve most of them.
### Our Code
If you are interested in the code and using it in your own project, you will find it on this page. Our code is free to use and edit. Attribution is not required.
