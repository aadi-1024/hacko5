import serial
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)
while True: 
    d = ser.readline().strip()
    print(d)

