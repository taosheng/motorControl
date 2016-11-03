#!/usr/bin/python

# a simple examlpe for control raver from USB of mac
# control char = w a d x s 
# must install pySerial module

import serial, time
s = serial.Serial('/dev/tty.usbserial-A500CNPN',9600)
while True:
    a = raw_input('--> ')
    print a
    s.write(a)
    line = s.readline()
    print line
        
#    response = serial.read()
#    print response
#ser.close()


