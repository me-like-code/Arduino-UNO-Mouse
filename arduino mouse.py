import serial
import pyautogui as pg

# pg.FAILSAFE = False

ser = serial.Serial("COM5", '9600')

while True:
    read = ser.readline().decode('ascii')
    array = read.split()
    print(array)

    x = int(array[2].replace(',', ''))
    y = (1439 - int(array[5].replace(',', '')))
    """"Since 0,0 is in the top left corner of
    the screen in pyautogui, we have to
    subtract the max screen height from
    the value of y.
    The minus 1 from the 1440 in the 
    y var to prevent the mouse from 
    triggering the failsafe."""
    pg.moveTo(int(x), int(y))
