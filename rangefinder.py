import wpilib

class MaxUltrasonic(wpilib.SensorBase):
    def __init__(self, channel):
        self.in_to_cm = 2.54
        self.use_units = True
        self.min_voltage = .5
        self.voltage_range = 5.0 - self.min_voltage
        self.min_distance = 3.0
        self.distance_range = 60.0 - self.min_distance
        self.channel = wpilib.AnalogInput(channel)

    def GetVoltage(self):
        return self.channel.getVoltage()

    def GetRangeInInches(self):
        range = self.GetRangeInCM()
        range /= self.in_to_cm

        return round(range, 2)

    def GetRangeInCM(self):
        
        range = self.channel.getVoltage()
        if not self.use_units:
            return -1.0
        elif range < self.min_voltage:
            return -2.0

        range = (range - self.min_voltage) / self.voltage_range
        range = (range * self.distance_range) + self.min_distance
        range *= self.in_to_cm
        range = round(range, 2)
        return range
