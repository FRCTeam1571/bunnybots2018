
#!/usr/bin/env python3
#Modified: 3/30

# For Solenoids:
# False = Up
# True = Down

import wpilib
from wpilib import drive, Timer, SendableChooser
import ctre
from networktables import NetworkTables
# import rangefinder



class robot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot Initiation'''
        self.controller = wpilib.XboxController(0)

        self.camServo = wpilib.Servo(0)


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
        while self.isAutonomous() and self.isEnabled():
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
        while self.isOperatorControl() and self.isEnabled():

            # Sets triggers and bumpers each loop
            self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
            self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
            self.BumperLeft = self.controller.getBumper(self.kLeft)
            self.BumperRight = self.controller.getBumper(self.kRight)

            print(self.controller.getX(self.kRight))
            self.camServo.set(self.controller.getX(self.kRight))
            # self.camServo.setAngle()


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
