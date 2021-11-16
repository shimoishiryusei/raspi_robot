from __future__ import print_function
from __future__ import division
from builtins import input
from BrickPi import *   #import BrickPi.py file to use BrickPi operations                                                                                                                                          
import readchar

BrickPiSetup()  # setup the serial port for communication                                                                                                                                                          

BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B                                                                                                                                                                
BrickPi.MotorEnable[PORT_C] = 1 #Enable the Motor C                                                                                                                                                                

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi                                                                                                                                                 

power = 0
power_l=0
power_r=0

while True:
        c=readchar.readkey()
        if c=='w':
            print ("Running Forward")
            power = 100
            BrickPi.MotorSpeed[PORT_B] = power  #Set the speed of MotorB (-255 to 255)                                                                                                                             
            BrickPi.MotorSpeed[PORT_C] = power  #Set the speed of MotorC (-255 to 255)                                                                                                                             

            #ot = time.time()                                                                                                                                                                                      
            #while(time.time() - ot < 3):    #running while loop for 3 seconds                                                                                                                                     
            BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors                                                                                                                          
                #time.sleep(.1)                                                                                                                                                                                    
        elif c=='a':
            print("Running Left")
            power_l = 100
            power_r = -100
            BrickPi.MotorSpeed[PORT_B] = power_l
            BrickPi.MotorSpeed[PORT_C] = power_r
            BrickPiUpdateValues()
        elif c=='d':
            print("Running Right")
            power_l = 100
            power_r = -100
            BrickPi.MotorSpeed[PORT_B] = power_r
            BrickPi.MotorSpeed[PORT_C] = power_l
            BrickPiUpdateValues()
        elif c=='s':
            print ("Running Backward")
            power = -100
            BrickPi.MotorSpeed[PORT_B] = power  #Set the speed of MotorB (-255 to 255)                                                                                                                             
            BrickPi.MotorSpeed[PORT_C] = power  #Set the speed of MotorC (-255 to 255)                                                                                                                             

            #ot = time.time()                                                                                                                                                                                      
            #while(time.time() - ot < 3):    #running while loop for 3 seconds                                                                                                                                     
            BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors                                                                                                                          
                #time.sleep(.1)              # sleep for 100 ms                                                                                                                                                    
                #keyboard.wait()                                                                                                                                                                                   
        elif c=='q':
                print("END")
                break
