#!/usr/bin/python3

# Control a robotic arm via an Arduino UNO
# Details on: https://homofaciens.de/technics-machines-robot-arm-v1-0_en.htm

import os
import sys     # Needed for handling command line parameters
import serial  # Needed for USB communication
import time
import tty
import termios
import select

#os.system("stty -echo")# Turn OFF keyboard echo

fileNameCoords = "StoredCoordinates.txt"
stepWidth = 1000;
stepWidthServos = 10;

joint_a = 0               # Rotation of arm
joint_b = 0               # UP/DOWN of arm
joint_c = 0               # Forward / Backward of arm
joint_e_default = 80      # Rotation of gripper
joint_d = joint_e_default
joint_e = 90              # Gripper

EOT = '\x04'  # CTRL+D
ESC = '\x1b'
CSI = '['

def write2USB(usbComm, command_line = "", wait_for_idle = 1):
    global joint_a
    global joint_b
    global joint_c
    global joint_d
    global joint_e

    # Empty read/write buffer
    usbComm.flush()

    print("Writing command: ", command_line)
    command_line = command_line + '\n' # Add new line char for Arduino
    usbComm.write(command_line.encode('utf-8'))# Write line to USB

    read_temp = " "
    read_byte = usbComm.read(1)
    while read_temp[-1] != "\\": # last byte received was '\n' (new line)
        read_temp = read_temp + str(read_byte)[2:3] # Wait for USB response
        read_byte = usbComm.read(1)
        #print("Received: ", str(read_temp), read_byte)
        #time.sleep(0.2)

    print("Received: ", str(read_temp))
    if read_temp.find("Ja:") > -1:
        joint_a = int(read_temp[read_temp.find("Ja:") + 3:read_temp.find("Jb:")])
    if read_temp.find("Jb:") > -1:
        joint_b = int(read_temp[read_temp.find("Jb:") + 3:read_temp.find("Jc:")])
    if read_temp.find("Jc:") > -1:
        joint_c = int(read_temp[read_temp.find("Jc:") + 3:read_temp.find("Jd:")])
    if read_temp.find("Jd:") > -1:
        joint_d = int(read_temp[read_temp.find("Jd:") + 3:read_temp.find("Je:")])
    if read_temp.find("Je:") > -1:
        joint_e = int(read_temp[read_temp.find("Je:") + 3:read_temp.rfind("\\")])

    print("joint_a=", joint_a, ", joint_b=", joint_b, ", joint_c=", joint_c, ", joint_d=", joint_d, ", joint_e=", joint_e)

    # Empty read buffer
    usbComm.flushInput()


def isKeyPressed():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def getchar():
    return sys.stdin.read(1)

def printHelp():
    print("\n\n")
    print("**************************************************")
    print("LEFT CURSOR:   rotate left")
    print("RIGHT CURSOR:  rotate right")
    print("UP CURSOR:     Backward")
    print("DOWN CURSOR:   Forward")
    print("PAGE UP:       move up")
    print("PAGE DOWN:     move down")
    print(">:             rotate servo joint d")
    print("<:             rotate servo joint d")
    print("o:             open gripper")
    print("c:             close gripper")
    print("Z:             set all coordinates to ZERO")
    print("s:             store current coordinates to file")
    print("p:             add pause line to stored coordinates file")
    print("D:             DELETE ALL strored coordinates")
    print("m:             Enable motors")
    print("M:             Disable motors")
    print("R:             replay strored coordinates")
    print("h:             print this help text")
    print("q:             quit")
    print("**************************************************")
    print("\n\n")

# Open USB port to Arduino
usbComm = serial.Serial(
# port = '/dev/ttyUSB0', #Replace ttyS0 with ttyACM0 for Pi1,Pi2,Pi0
port = '/dev/ttyACM0', #Replace ttyACM0 with ttyUSB0 for Pi3 and Pi4
baudrate = 115200,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize = serial.EIGHTBITS,
timeout = 1
)
time.sleep(1.002)# Give port some time to really open...

old_settings = termios.tcgetattr(sys.stdin)

printHelp()

try:
    tty.setcbreak(sys.stdin.fileno())
    doLoop = True

    while doLoop:
        c = ''

        while not isKeyPressed():
            pass

        c = getchar()

        if c == EOT or c == "q" or c == 'Q':
            print("Really EXIT script (Y/N)?")
            answer = getchar().upper()
            while answer != 'Y' and answer != 'N':
                answer = getchar().upper()
            if answer == 'Y':
                print('exit')
                doLoop = False
            else:
                print("continuing...")

        elif c == ESC: # Special characters
            x = getchar()
            if x == CSI:
                x = getchar()
                if x == 'A':
                    print('UP')
                    command_line = "jb " + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                elif x == 'B':
                    print('DOWN')
                    command_line = "jb -" + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                elif x == 'C':
                    print('RIGHT')
                    command_line = "ja " + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                elif x == 'D':
                    print('LEFT')
                    command_line = "ja -" + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                elif x == '5':
                    print('PAGE UP')
                    x = getchar()
                    command_line = "jc -" + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                elif x == '6':
                    print('PAGE DOWN')
                    x = getchar()
                    command_line = "jc " + str(stepWidth)
                    write2USB(usbComm, command_line)# Write line to USB
                else:
                    print("Special key is ", x)
            if x == ESC:
                print("Really EXIT script (Y/N)?")
                answer = getchar().upper()
                while answer != 'Y' and answer != 'N':
                    answer = getchar().upper()
                if answer == 'Y':
                    print('exit')
                    doLoop = False
                else:
                    print("continuing...")

        elif c == 's':
            storeFile = open(fileNameCoords, "a")
            storeFile.write("Ja " + str(joint_a) + " Jb " + str(joint_b) + " Jc " + str(joint_c) + " Jd " + str(joint_d) + " Je " + str(joint_e) + "\n")
            print("Coordinates stored!")
            storeFile.close()

        elif c == 'p':
            storeFile = open(fileNameCoords, "a")
            storeFile.write("P1.1\n")
            print("Pause added to stored Coordinates file!")
            storeFile.close()

        elif c == '<': # Servo joint d
            command_line = "jd " + str(stepWidthServos)
            write2USB(usbComm, command_line)# Write line to USB

        elif c == '>': # Servo joint d
            command_line = "jd -" + str(stepWidthServos)
            write2USB(usbComm, command_line)# Write line to USB

        elif c == 'o': # Open gripper
            command_line = "Je 50"
            write2USB(usbComm, command_line)# Write line to USB

        elif c == 'c': # Close gripper
            command_line = "Je 110"
            write2USB(usbComm, command_line)# Write line to USB

        elif c == 'Z':
            print("Set all coordinates to ZERO (Y/N)?")
            answer = getchar().upper()
            while answer != 'Y' and answer != 'N':
                answer = getchar().upper()
            if answer == 'Y':
                write2USB(usbComm, "ZZ")# Write line to USB
                print("All coordinates set to ZERO points!")
            else:
                print("NOT set to zero.")

        elif c == 'D':
            print("DELETE ALL stored coordinates (Y/N)?")
            answer = getchar().upper()
            while answer != 'Y' and answer != 'N':
                answer = getchar().upper()
            if answer == 'Y':
                storeFile = open(fileNameCoords, "w")
                print("All coordinates deleted!")
                storeFile.close()
            else:
                print("Stored coordinates NOT deleted.")

        elif c == '0':
            print("Driving to ZERO...")
            write2USB(usbComm, "Ja 0 Jb 0 Jc -10000 Jd " + str(joint_e_default) + " Je 90", 1)# Write line to USB
            write2USB(usbComm, "Ja 0 Jb 0 Jc 0 Jd " + str(joint_e_default) + " Je 90", 1)# Write line to USB
            print("...done!")

        elif c == 'm':
            print("Enable motors.")
            write2USB(usbComm, "EN")# Write line to USB

        elif c == 'M':
            print("DISABLE motors.")
            write2USB(usbComm, "DIS")# Write line to USB

        elif c == '+':
            if stepWidth == 1000:
                stepWidth = 5000
                stepWidthServos = 20
            if stepWidth == 100:
                stepWidth = 1000
                stepWidthServos = 10
            print("stepWidth=", stepWidth, ", stepWidthServos=", stepWidthServos)

        elif c == '-':
            if stepWidth == 1000:
                stepWidth = 100
                stepWidthServos = 1
            if stepWidth == 5000:
                stepWidth = 1000
                stepWidthServos = 10
            print("stepWidth=", stepWidth, ", stepWidthServos=", stepWidthServos)

        elif c == 'R':
            print("Replaying coordinates...")
            storeFile = open(fileNameCoords, "r")
            lines = storeFile.readlines()
            for line in lines:
                if line[0:1] == "P":
                    print("Pause for ", float(line[1:]), "seconds")
                    time.sleep(float(line[1:]))
                else:
                    print("Going to ", line)
                    write2USB(usbComm, line[:-1], 1)# Strip trailing \n from line
                    #time.sleep(1.0)
                if isKeyPressed():
                    print("Really abort replay (Y/N)?")
                    answer = getchar().upper()
                    while answer != 'Y' and answer != 'N':
                        answer = getchar().upper()
                    if answer == 'Y':
                        print('Replay aborted!')
                        break
                    else:
                        print("continuing...")
            storeFile.close()
            print("...done!")

        elif c == 'h':
            printHelp()

        elif c == '':
            print("Nothing...\n")
            time.sleep(0.5)

        else:
            print("You have pressed ", c)

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    #os.system("stty echo")# Turn ON keyboard echo
    usbComm.close()
    print("...done!")
