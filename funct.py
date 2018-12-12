import wpilib

def numMap(x, in_min, in_max, out_min, out_max):
    '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class ColorSensor():
    def __init__(self, OUT, OE, S0, S1, S2, S3):
        self.OUT = wpilib.Counter(OUT)
        self.OE = wpilib.DigitalOutput(OE)
        #Frequencies
        self.S0 = wpilib.DigitalOutput(S0)
        self.S1 = wpilib.DigitalOutput(S1)
        #Colours
        self.S2 = wpilib.DigitalOutput(S2)
        self.S3 = wpilib.DigitalOutput(S3)

        self.maxVal = 1000000 # Max output value
        

        self.S0.set(True) # 100% Output Frequency
        self.S1.set(True)


    def setColor(self, rgba):
        if rgba == 'red':
            self.S2.set(False)
            self.S3.set(False)
        elif rgba == 'blue':
            self.S2.set(False)
            self.S3.set(True)
            print("blue")
        elif rgba == 'clear':
            self.S2.set(True)
            self.S3.set(False)
        elif rgba == 'green':
            self.S2.set(True)
            self.S3.set(True)
        else:
            print("Error: RGBA Value Not Accepted")
    
    def setFrequency(self, freq):
        if freq == 0:
            self.S0.set(False)
            self.S1.set(False)
        elif freq == 2:
            self.S0.set(False)
            self.S1.set(True)
        elif freq == 20:
            self.S0.set(True)
            self.S1.set(False)
        elif freq == 100:
            self.S0.set(True)
            self.S1.set(True)
        else:
            print("Error: Frequency Value Not Accepted")

    def setMaxValue(self, value):
        self.maxVal = value
        



    def getValue(self):
        # 100000 Max
        # 0 Min
        frequency = 1 / (self.OUT.getPeriod() / 2) # Gets Frequency. getPeriod() displays the length of two periods, and frequency is equal to 1 / period
        mapFreq = numMap(frequency, 0, 1000000, 0, 1000)
        
        return mapFreq
        
def colorSorter(self):
    print(self.colorSensor.getValue())
    if not self.haveColor:
        print("Nice")
        if self.colorSensor.getValue() <= 150 and self.colorSensor.getValue() >= 200: # If the color sensor detects red
            self.haveColor = True
            if self.correctColor == "r":
                self.sortMotor.set(-0.5)
            else:
                self.sortMotor.set(0.5)
        if self.colorSensor.getValue() <= 100 and self.colorSensor.getValue() > 150: # If the color sensor detects blue
            self.haveColor = True
            if self.correctColor == "b":
                self.sortMotor.set(-0.5)
            else:
                self.sortMotor.set(0.5)

    if self.sortSwitch.get() and self.haveColor:
        self.haveColor = False
        self.sortMotor.set(0.0)
        