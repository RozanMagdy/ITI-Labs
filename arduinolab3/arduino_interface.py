from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 
while True:
     DATA = ser.readline() # Read the newest output from the Arduino
     print(DATA)
     sleep(.1) # Delay for one tenth of a second
