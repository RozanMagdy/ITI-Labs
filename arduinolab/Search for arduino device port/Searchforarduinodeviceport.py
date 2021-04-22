import os
from time import sleep
import serial
os.system('udevadm info -e > USBDevicesData.txt')
f = open('USBDevicesData.txt', "r")
lines=f.read().splitlines()
for line_index in range(len(lines)):
    if 'DEVPATH' in lines[line_index] and 'ttyACM0' in lines[line_index]:
       print('USB Port Number: '+lines[line_index].split('/')[4])
       print('Device Type: '+lines[line_index+12].split('=')[1])
       print('Device Class: '+lines[line_index+13].split('=')[1])
       print('Device Serial: '+lines[line_index+20].split('=')[1])
       ser = serial.Serial('/dev/ttyACM0', 9600) 
       while True:
            print (ser.readline()) # Read the newest output from the Arduino
            sleep(.1) # Delay for one tenth of a second
       