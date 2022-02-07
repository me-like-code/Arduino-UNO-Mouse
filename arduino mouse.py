from serial import Serial
from pyautogui import moveTo

s = Serial('COM5', '9600')

'''Since 0,0 is in the top left corner of
the screen in pyautogui, we have to
subtract y from the max screen height'''

while True:
    read = s.readline().decode('ASCII')
    array = read.split()
    x = int(array[0])
    y = 1439-int(array[1])
    moveTo(int(x), int(y), 0.01)

