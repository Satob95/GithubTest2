import serial

arduinoData=serial.Serial(port='/dev/cu.usbmodem141201', baudrate=9600) #port angabe evtl nicht richtig?
#(port='/dev/cu.usbmodem141201', baudrate=9600) is medial USB port in mac-adapter
#

def stimulation_ON():
    arduinoData.write(b'1')
    #writes 1 to the serial port, which is connected to the arduino.
    #whatever happens, when 1 is transmitted is defined in the arduino code
    #in this case: activation of the connected device

def stimulation_OFF():
    arduinoData.write(b'2')
    #inactivates the connected device

#t=0
#while(t<50): #baut ein kurzes delay ein!
#    if(t%10==0):
#        print(t)
#    t+=1

while True:
    command = input("Enter command (1 to switch On/Off): ")
    print ("you entered " + command)
    
    if (command=='1'):
        stimulation_ON()
        print("Stimulation turned on")
        
    elif (command=='2'):
        stimulation_OFF()
        print("Stimulation turned off")
        

