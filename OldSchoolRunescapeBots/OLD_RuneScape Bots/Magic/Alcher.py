import pyautogui
import random
import time
print('Make sure your items are in the same place as cast alch and u are on youyr spell book')
print('How many alchs would you like to do?')
numAlchs = input()
print('put cursor over alch area!!! You have 3 seconds before this starts!')
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
i=0
justPaused = False
try:
    while i<numAlchs:
        i+=1
        print('Alch Number '+str(i))
        pyautogui.click(pyautogui.position())
        time.sleep(1.8+random.uniform(0, 0.6))
        pyautogui.click(pyautogui.position())
        time.sleep(1.8+random.uniform(0, 0.3))
        randPause = random.randint(0, 1000)
        if (randPause == 500):
            if(justPaused==False):
                time.sleep(187+random.uniform(0,96))
                justPaused=True
            else:
                print('Skipped double pause')
                justPaused==False
        if(randPause==101) or (randPause==102):
            if(justPaused==False):
                time.sleep(10+random.uniform(0,10))
                justPaused=True
            else:
                print('Skipped double pause')
                justPaused==False
except KeyboardInterrupt:
    print('Stopping')
