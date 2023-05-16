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
