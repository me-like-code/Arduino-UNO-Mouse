import serial
from pyautogui import moveTo

# pg.FAILSAFE = False

s = serial.Serial("COM5", '9600')

""""Since 0,0 is in the top left corner of
the screen in pyautogui, we have to
subtract the max screen height from
the value of y"""

while True:
    read = s.readline().decode('ascii')
    array = read.split()
    x = int(array[0])
    y = 1440-int(array[1])
    moveTo(int(x), int(y))
