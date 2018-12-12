
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
import rangefinder



class robot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot Initiation'''
        self.controller = wpilib.XboxController(0)

        # wpilib.CameraServer.launch()

        # self.intake = wpilib.Talon(0)

        self.colorSensor = funct.ColorSensor(10, 11, 12, 13, 14, 15)
        self.colorSensor.setColor("clear")
        self.correctColor = 'r' # Color for the color sensor to look for
        self.sortSwitch = wpilib.DigitalInput(0)

        self.sortMotor = wpilib.Talon(0) ## !! CHANGE TO TALON !! ##

        self.rf = rangefinder.MaxUltrasonic(0)

        # Talon SRX #
        # Right drivetrain
        # self.fr_motor = ctre.wpi_talonsrx.WPI_TalonSRX(2)  # 2
        # self.rr_motor = ctre.wpi_talonsrx.WPI_TalonSRX(3)  # 3
        # self.right = wpilib.SpeedControllerGroup(self.fr_motor, self.rr_motor)

        # # Left drivetrain
        # self.fl_motor = ctre.wpi_talonsrx.WPI_TalonSRX(0)  # 0
        # self.rl_motor = ctre.wpi_talonsrx.WPI_TalonSRX(1)  # 1
        # self.left = wpilib.SpeedControllerGroup(self.fl_motor, self.rl_motor)

        # self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def disabledInit(self):
        self.haveColor = False
        # self.timer.reset()
        # self.timer.start()


    def disabledPeriodic(self):
        pass

        



    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.haveColor = False
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
        self.haveColor = False
        # self.timer.reset()
        # self.timer.start()




    def teleopPeriodic(self):

        """This function is called periodically during operator control."""
        # Sets triggers and bumpers each loop
        self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
        self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
        self.BumperLeft = self.controller.getBumper(self.kLeft)
        self.BumperRight = self.controller.getBumper(self.kRight)


        funct.colorSorter(self)
        # Color Sensor Test #
        # print(round(self.colorSensor.getValue(), 2))

        # if self.controller.getXButton() and not self.GrabLast:
        #     self.GrabToggle = not self.GrabToggle

        # self.GrabLast = self.controller.getXButton()
  
        # if self.GrabToggle and self.GrabLast:
        #     self.grab.set(True)
        # elif self.GrabLast:
        #     self.grab.set(False)

        # Drive System #
        # backwards control
        # if self.BumperLeft:
        #     self.TriggerLeft = self.TriggerLeft * -1
        
        # # Drive #
        # self.drive.arcadeDrive(self.TriggerLeft, self.controller.getX(self.kLeft))


#Runs function upon ready
if __name__ == "__main__":
    wpilib.run(robot,
            physics_enabled=True)
