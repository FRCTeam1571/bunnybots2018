import wpilib

def numMap(x, in_min, in_max, out_min, out_max):
    '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class ColorSensor():
    def __init__(self, OUT, OE, S0, S1, S2, S3):
        self.OUT = wpilib.Counter(OUT)
        self.OE = wpilib.DigitalOutput(OE)
        self.S0 = wpilib.DigitalOutput(S0)
        self.S1 = wpilib.DigitalOutput(S1)
        self.S2 = wpilib.DigitalOutput(S2)
        self.S3 = wpilib.DigitalOutput(S3)
        

        # self.OUT.setUpdateWhenEmpty(True) # Want output to be 0 when output is stalled

        self.S0.set(True) # 100% Output Frequency
        self.S1.set(True)

        self.S2.set(False) # Red
        self.S3.set(False)

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
            self.S2.set(True)
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
        



    def getColor(self):
        
        # return self.OUT.getRaw()
        return self.OUT.getPeriod()
        
