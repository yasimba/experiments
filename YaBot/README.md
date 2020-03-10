
## Table of Contents
1. [Introduction](#introduction)
2. [Parts](#parts)
3. [Assembly](#assembly)
5. [Testing](#testing)

## Introduction

![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/robot_sketch_bb.jpg)

## Parts


## Assembly

Below is the breadboard design:

* The quickstart assembly was done in the following way without a breadboard ----->

* Below are the parts needed to build the robot. They include; 2 Wheels, the L298N H-Bridge Dual-Stepper Motor driver, 2 motors, the Robot Chasis and wires/bolts needed to put the robot together
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/1.jpg)

*  I started by placing the motors in place and screwing them with a screw driver
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/2.jpg)

* Then, I snapped the wheels in place
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/3.jpg)

* In the future I would like to make the robot movements precise and smart by using various methods such as PID control. Thus, I latched encoders onto the wheels.
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/4.jpg)

* I had the option of adding a switch to the chasis to control the power supply for the motors. However, I may not need it.
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/5.jpg)

* Here we have the 4*AAA battery holder to supply the required 12V to drive the motors.
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/6.jpg)

* The L298N stepper motor driver is attached here.
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/7.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/8.jpg)

* Now we connect the Pi3
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/9.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/10.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/11.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/12.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/13.jpg)

* Finally, the robot is complete. We have 2 problems though:
1. How can be control the robot wirelessly
2. How can we power the Pi3 such that the robot is not limited in movement by a power supply wire.

To solve the wireless control, I configured the Pi to connect headlessly to my router. This config can be found in the wpa_config file in the root directory of the Pi. The power supply problem was resolved using a power bank that we can place ontop of the Pi. Doing this, we have the following results:
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/14.jpg)
![](https://raw.githubusercontent.com/yasimba/YaBot/master/documentation/16.jpg)

## Testing

* Run the code in `software/test_code.py`. The robot should now be able to move programmatically
