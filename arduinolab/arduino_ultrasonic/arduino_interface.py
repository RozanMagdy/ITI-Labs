from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 
while True:
     print (ser.readline()) # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
