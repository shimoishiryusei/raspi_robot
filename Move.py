from __future__ import print_function
from __future__ import division
from builtins import input
from BrickPi import*  # import BrickPi.py file to use BrickPi operations
import readchar
import time

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1  # R
BrickPi.MotorEnable[PORT_C] = 1  # L
BrickPi.MotorEnable[PORT_A] = 1  # migihasi

BrickPiSetupSensors()  # Send the properties of sensors to BrickPi

power = 200

while True:
    c = readchar.readkey()
    if c == 'h':
        power = 255
        print("speed", power)
    elif c == 'j':
        power = 200
        print("speed", power)
    elif c == 'k':
        power = 150
        print("speed", power)
    elif c == 'l':
        power = 80
        print("speed", power)
    elif c == 'w':
        print("Running Forward")
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        BrickPi.MotorSpeed[PORT_B] = power
        BrickPi.MotorSpeed[PORT_C] = power
        BrickPiUpdateValues()
    elif c == 'a':
        print("Running Left")
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        BrickPi.MotorSpeed[PORT_B] = power
        BrickPi.MotorSpeed[PORT_C] = -1*(power-40)
        BrickPiUpdateValues()
    elif c == 'd':
        print("Running Right")
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        BrickPi.MotorSpeed[PORT_B] = -1*(power-40)
        BrickPi.MotorSpeed[PORT_C] = power
        BrickPiUpdateValues()
    elif c == 's':
        print("Running Backward")
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        BrickPi.MotorSpeed[PORT_B] = -1*power
        BrickPi.MotorSpeed[PORT_C] = -1*power
        BrickPiUpdateValues()
    elif c == ' ':
        print("Attack")
        power = 255
        BrickPi.MotorSpeed[PORT_A] = 0
        BrickPi.MotorSpeed[PORT_A] = power
        BrickPiUpdateValues()
        time.sleep(0.2)

        BrickPi.MotorSpeed[PORT_A] = 0
        BrickPi.MotorSpeed[PORT_A] = -1*power
        BrickPiUpdateValues()
    elif c == 'q':
        print("END")
        break
