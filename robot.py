
#!/usr/bin/env python3
#Modified: 3/30

# For Solenoids:
# False = Up
# True = Down

import wpilib
from wpilib import drive, Timer, SendableChooser
import ctre
from networktables import NetworkTables
import funct
# import rangefinder



class robot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot Initiation'''
        self.controller = wpilib.XboxController(0)

        # wpilib.CameraServer.launch('vision.py:main')

        self.camServo = wpilib.Servo(0)
        # self.solenoid = wpilib.Solenoid(1)
        self.doorMotor = wpilib.Talon(1)
        self.nidec = wpilib.NidecBrushless(2, 0)

    def disabledInit(self):
        pass
        # self.timer.reset()
        # self.timer.start()


    def disabledPeriodic(self):
        pass

        # Ultrasonic test #
        # if self.timer.get() >= 2.0:
        #     self.timer.reset()
        #     self.timer.start()
        #     self.table.putNumber('Range In Inches', self.ultrasonic.GetRangeInInches(self))


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass
        # self.timer.reset()
        # self.timer.start()
        # self.select = self.chooser.getSelected()


    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        # Drive for two seconds
        pass


    def teleopInit(self):
        """This function is run once each time the robot enters teleop mode"""
        self.kLeft = self.controller.Hand.kLeft
        self.kRight = self.controller.Hand.kRight
        # self.timer.reset()
        # self.timer.start()




    def teleopPeriodic(self):

        """This function is called periodically during operator control."""

        # Sets triggers and bumpers each loop
        self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
        self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
        self.BumperLeft = self.controller.getBumper(self.kLeft)
        self.BumperRight = self.controller.getBumper(self.kRight)

        servoMap = funct.numMap(self.controller.getX(self.kRight), -1.0, 1.0, 0.0, 1.0)
        self.camServo.set(servoMap)
        # self.camServo.setAngle()
        # if self.controller.getAButton():
        #     self.solenoid.set(True)
        if self.controller.getBButton():
            self.doorMotor.set(0.5)
        else:
            self.doorMotor.set(0.0)

        if self.controller.getYButton():
            self.nidec.set(0.5)
            # print(self.nidec.getDescription())
        else:
            self.nidec.set(0.0)



        # Drive System #
        # backwards control
        # if self.BumperLeft:
        #     self.TriggerLeft = self.TriggerLeft * -1
        #
        # # Drive #
        # self.drive.arcadeDrive(self.TriggerLeft, self.controller.getX(self.kLeft))



if __name__ == "__main__":
    wpilib.run(robot,
            physics_enabled=True)
