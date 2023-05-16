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
