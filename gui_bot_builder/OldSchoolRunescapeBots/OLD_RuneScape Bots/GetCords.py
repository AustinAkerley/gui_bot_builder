import pyautogui
import random
import time
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
try:
    while True:
        time.sleep(.33333)
        print(pyautogui.position())
except KeyboardInterrupt:
    print('Stopping')
