import wpilib

def numMap(x, in_min, in_max, out_min, out_max):
    '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class ColorSensor():
    def __init__(self, S0, S1, S2, S3, OUT, OE):
        self.S0 = wpilib.PWM(S0)
        self.S1 = wpilib.PWM(S1)
        self.S2 = wpilib.PWM(S2)
        self.S3 = wpilib.PWM(S3)
        self.OUT = wpilib.PWM(OUT)
        self.OE = wpilib.PWM(OE)

        self.S0.setRaw(0)
        self.S1.setRaw(255)

        self.S2.setRaw(0)
        self.S3.setRaw(0)

    def setColor(self, rgba):
        if rgba == 'red':
            self.S2.setRaw(0)
            self.S3.setRaw(0)
        elif rgba == 'blue':
            self.S2.setRaw(0)
            self.S3.setRaw(255)
        elif rgba == 'clear':
            self.S2.setRaw(255)
            self.S3.setRaw(0)
        elif rgba == 'green':
            self.S2.setRaw(255)
            self.S2.setRaw(255)
        else:
            print("Error: RGBA Value Not Accepted")
    
    def setFrequency(self, freq):
        if freq == 0:
            self.S0.setRaw(0)
            self.S1.setRaw(0)
        elif freq == 2:
            self.S0.setRaw(0)
            self.S1.setRaw(255)
        elif freq == 20:
            self.S0.setRaw(255)
            self.S1.setRaw(0)
        elif freq == 100:
            self.S0.setRaw(255)
            self.S1.setRaw(255)
        else:
            print("Error: Frequency Value Not Accepted")
        



    def getColor(self):
        return self.OUT.getRaw()
        
