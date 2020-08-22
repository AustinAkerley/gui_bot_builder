import pyautogui
import random
import time

wee =4
if 2<wee<8:
    print('HIIIIIIIIII')

time.sleep(3)
width, height = pyautogui.size()
pyautogui.click(1492+random.randint(0,3), 51+random.randint(0,3))
# Reset using mouse movements and stuff
pyautogui.click(1505, 96)
time.sleep(6.5)
pyautogui.click(1508, 118)
time.sleep(6.5)
pyautogui.click(1639, 109)
time.sleep(6.5)
pyautogui.click(1628, 144)
time.sleep(6.5)
pyautogui.click(1567, 117)
time.sleep(6.5)
