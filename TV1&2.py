# Import the tkinter library for GUI
import tkinter as tk

class TV:
# Use def function to initialize the channel and volume
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1

# Method to turn off and on the tv
    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

# Set the channel
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def getChannel(self):
        return self.channel
    
# Set the volume of the channel
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def getVolume(self):
        return self.volumeLevel
    
# Set the channel up and down by 1, set maximum and maximum
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

# Set the volume up and down by 1, set maximum and maximum
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

# Create tv object 1 and 2, turn on, set channel and set volume
    def __init__(self):
        self.tv1 = TV()
        self.tv2 = TV()
        self.tv1.turnOn()
        self.tv2.turnOn()
        self.tv1.setChannel(30)
        self.tv1.setVolume(3)
        self.tv2.setChannel(3)
        self.tv2.setVolume(2)
        self.create_ui()

# Adjust channel and volume
    def channel_up_tv1(self):
        self.tv1.channelUp()
        self.update_labels()

    def channel_down_tv1(self):
        self.tv1.channelDown()
        self.update_labels()

    def volume_up_tv1(self):
        self.tv1.volumeUp()
        self.update_labels()

    def volume_down_tv1(self):
        self.tv1.volumeDown()
        self.update_labels()

    def channel_up_tv2(self):
        self.tv2.channelUp()
        self.update_labels()

    def channel_down_tv2(self):
        self.tv2.channelDown()
        self.update_labels()

    def volume_up_tv2(self):
        self.tv2.volumeUp()
        self.update_labels()

    def volume_down_tv2(self):
        self.tv2.volumeDown()
        self.update_labels()

    def update_labels(self):
        self.tv1_channel_label.config(text=f"tv1's channel is {self.tv1.getChannel()}")
        self.tv1_volume_label.config(text=f"Volume level is {self.tv1.getVolume()}")
        self.tv2_channel_label.config(text=f"tv2's channel is {self.tv2.getChannel()}")
        self.tv2_volume_label.config(text=f"Volume level is {self.tv2.getVolume()}")

    def create_ui(self):
        root = tk.Tk()
        root.title("TV Simulator")
        root.geometry("1200x600")

# Create TV1 frame
        tv1_frame = tk.Frame(root)
        tv1_frame.pack(side="left", padx=20)

# Create TV1 channel label
        self.tv1_channel_label = tk.Label(tv1_frame, text=f"Tv1's channel is {self.tv1.getChannel()}",font=("Times new roman", 18))
        self.tv1_channel_label.pack()

# Create TV1 volume label
        self.tv1_volume_label = tk.Label(tv1_frame, text=f"Volume level is {self.tv1.getVolume()}",font=("Times new roman", 18))
        self.tv1_volume_label.pack()