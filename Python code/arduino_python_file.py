#prerequiriements
#pip install opencv-python
#pip install pyserial
import time
import serial
import cv2

arduino_ser = serial.Serial('COM4', 9600, timeout=1) # ensure the 'COM#' corresponds to the port that worked with the Arduino IDE.
time.sleep(2)
imgLedOn = cv2.imread("../Output/LedOn.png")
imgLedOff = cv2.imread("../Output/LedOff.png")

while True:
    arduino_ser.write(b'H')   # send a byte
    cv2.imshow('Image', imgLedOn)
    # wait 3 seconds
    cv2.waitKey(3000)
    arduino_ser.write(b'L')   # send a byte
    cv2.imshow('Image', imgLedOff)
    # wait 1 seconds
    cv2.waitKey(1000)

arduino_ser.close()
