# bunnybots2018
Robot code for BunnyBots 2018: "Pack 'Em Up"

Based on code from [FRCTeam1571/robot2018](https://github.com/FRCTeam1571/robot2018)

##### Deploy code via USB:
- Connect RoboRIO to computer with USB A to USB B cable
- In command line type: `py robot.py --skip-tests --robot 172.22.11.2`
##### Deploy code via WiFi / Using Robot wirelessly (Windows):
- If after main FRC competition:
  - Launch FRC Radio Configuration Utility
  - Connect Ethernet cable from computer to the robot's radio
  - Follow steps given by utility, use team number 1571
  - Disconnect Ethernet cable after finished
- Launch Control Panel
- Click 'Network and Sharing Center'
- Click 'Connections' then 'Properties'
- Select 'Internet Protocol Version 4 (TCP/ IP v4)', double click
- Click 'Use following IP address:'
- Input `10.15.71.2` into IP address field and `255.0.0.0` into Subnet mask
- Click Ok on the last two windows
- Click on WiFi button on the toolbar and wait for the WiFi Network to show up. Connect to it.
- If communications do not connect for some time:
  - On the Connection Status window, click the button that says 'Diagnose'. Have Windows fix any problems it finds.
###### Deploy
- Once connected, type `py robot.py --skip-tests --robot 10.15.71.2` into the command line
