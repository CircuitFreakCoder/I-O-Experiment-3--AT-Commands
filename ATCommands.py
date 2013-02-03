"""
Opening and Closing Application through SMS
and Sending Confirmation Text to the Sender

Coded by Jorick Caberio
PUP BSCoE
August 24, 2012
"""

import os, sys, serial, time
from Tkinter import *

#closing file
def Close(target2):
    os.system("TASKKILL /F /IM "+target2)
    print 'closed '+target2

#GUI

def GUI(Message):
    global app
    app = Tk()
    app.title('IO Experiment 3: Open Application through SMS')
    app.geometry('450x300+350+400')
    labeltext = StringVar()
    labeltext.set(Message)
    label1 = Label(app, textvariable = labeltext, height =20)
    label1.pack()
    app.mainloop()

#main
buf =''
SerialPort = serial.Serial("COM29",115200)
SerialPort.write('AT+CMGF=1\r')
time.sleep(1)
r1 = SerialPort.read(SerialPort.inWaiting())
print buf+r1
SerialPort.write('AT+CMGR=0\r\n')
time.sleep(1)
r2 = SerialPort.read(SerialPort.inWaiting())
buf = buf + r2
print buf

#added codes to determine the texter
buf1 = buf.split()
buf2 =buf1[2]
print buf2
buf3 = buf2.split(",")
print buf3
buf4 = buf3[1]
print "texter is " +buf4
texter = buf4

#added code to determine message keyword
buf1 = buf.split()
buf5 =buf1[3]
keyword = str(buf5)
SerialPort.write('AT+CMGD=0\r\n')
SerialPort.close()
print "keyword is "+keyword
choice1 = "Z80" in keyword
choice2 = "CircuitWiz" in keyword
choice3 = "Arduino" in keyword
choice4 = "CloseApp" in keyword

if choice1 == True:
    print "you choose Z80"
    os.startfile(r'"C:\Program Files\Z80 Simulator IDE\z80simulatoride.exe"')
    SerialPort = serial.Serial("COM29",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS='+texter+'\r\n')
    time.sleep(1)
    SerialPort.write("you opened Z80 Emulator\x1A")
    time.sleep(1)
    print 'message sent'
    GUI("you opened Z80 Emulator")

elif choice2 == True:
    print "you choose Circuit wizard"
    os.startfile(r'"C:\Program Files\New Wave Concepts\Circuit Wizard\CktWiz.exe"')
    SerialPort = serial.Serial("COM29",115200)

SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS='+texter+'\r\n')
    time.sleep(1)
    SerialPort.write("you opened Circuit Wizard\x1A")
    time.sleep(1)
    print 'message sent'
    GUI("you opened Circuit Wizard")

elif choice3 == True:
    print "you choose Arduino"
    os.startfile(r'"C:\Users\Jorick\Downloads\arduino-1.0.1-windows\arduino-1.0.1\arduino.exe"')
    SerialPort = serial.Serial("COM29",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS='+texter+'\r\n')
    time.sleep(1)
    SerialPort.write("you opened Arduino IDE\x1A")
    time.sleep(1)
    print 'message sent'
    GUI("you opened Arduino IDE")

elif choice4 == True:
    print "you closed the app"
    Close("z80simulatoride.exe")
    Close("javaw.exe")
    Close("CktWiz.exe")
    SerialPort = serial.Serial("COM29",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS='+texter+'\r\n')
    time.sleep(1)
    SerialPort.write("you closed the application\x1A")
    time.sleep(1)
    print 'message sent'
    GUI("you closed the application")

else:
    print "invalid keyword"
    SerialPort = serial.Serial("COM29",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS="+639278537442"\r\n')
    time.sleep(1)
    SerialPort.write("Invalid keyword\x1A")
    time.sleep(1)
    print 'message sent'
    GUI("Invalid Keyword")


