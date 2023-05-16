# Tv1_and_TestTV
A Python code for creating the class named TV and a test driver program named TestTV

## Table of contents
* [Program Description](#program-description)
* [Functionalities](#functionalities)
* [General info](#general-info)

## Program Description
The TV Simulator program is a graphical user interface (GUI) application that simulates the functionality of two televisions (TVs). The program is built using the tkinter library in Python. Each TV object has the ability to turn on/off, change channels, and adjust the volume level.

## Functionalities
TV Class:
turnOn(): Turns on the TV.
turnOff(): Turns off the TV.
setChannel(channel): Sets the channel of the TV.
getChannel(): Returns the current channel of the TV.
setVolume(volumeLevel): Sets the volume level of the TV.
getVolume(): Returns the current volume level of the TV.
channelUp(): Increases the channel by one.
channelDown(): Decreases the channel by one.
volumeUp(): Increases the volume level by one.
volumeDown(): Decreases the volume level by one.
TestTV Class:
Initializes two TV objects (tv1 and tv2).
Sets initial values for channel and volume for both TVs.
Creates a GUI to display the TV controls and current channel/volume information.
Defines methods to handle button presses for controlling the TVs:
channel_up_tv1(), channel_down_tv1(), volume_up_tv1(), volume_down_tv1(): Control TV 1.
channel_up_tv2(), channel_down_tv2(), volume_up_tv2(), volume_down_tv2(): Control TV 2.
update_labels(): Updates the channel and volume labels on the GUI.
create_ui(): Creates the graphical user interface using tkinter.
Instantiates the TestTV class to run the program.

## General info
Overall, the TV Simulator program provides a visual representation of two TVs and allows the user to interact with them by changing channels and adjusting the volume using the provided GUI controls.
	