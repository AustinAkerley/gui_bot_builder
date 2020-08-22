import pyautogui
import random
import time

width, height = pyautogui.size()
timeOperational = 10 
i=0
try:
    while i <= 6*timeOperational :
        totalTenMinutes = 60*10
        timeLeft = totalTenMinutes
        print ('Time operational thus far: '+ str(i*10) + ' minutes')
        waitTime = 250+random.randint(0,100)
        print('First Wait Time: '+str(waitTime))
        timeLeft-=waitTime
        time.sleep(waitTime)
        leftOrRight = random.randint(0,1) #If 0 left if 1 right
        if(leftOrRight==0):
            pyautogui.keyDown('left')
            waitTime = 1+random.uniform(0,1)
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('left')
        else:
            pyautogui.keyDown('right')
            waitTime = 1+random.uniform(0,1)
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('right')
        waitTime = 4+random.uniform(0,5)
        timeLeft -= waitTime
        time.sleep(waitTime)
          
        leftOrRight = random.randint(0,1) 
        if(leftOrRight==0):
            pyautogui.keyDown('left')
            waitTime = 1+random.uniform(0,1)
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('left')
        else:
            pyautogui.keyDown('right')
            waitTime = 1+random.uniform(0,1)
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('right')
        time.sleep(timeLeft+random.uniform(0,20))
except KeyboardInterrupt:
    print('Ending loop with keyboard interrupt')
