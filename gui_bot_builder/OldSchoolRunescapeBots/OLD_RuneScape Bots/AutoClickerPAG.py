import pyautogui
import random
import time

width, height = pyautogui.size()
# Set time variable (a.k.a. time that this program should run)
timeOperational = 10 #in hours
i=0
# Begin Loop
try:
    while i <= 6*timeOperational :
        totalTenMinutes = 60*10
        timeLeft = totalTenMinutes
        print ('Time operational thus far: '+ str(i*10) + ' minutes')
        # Wait 10 minutes
        # Wait some random amount of time and take it out of the total ten minutes
        waitTime = 250+random.randint(0,100)
        print('First Wait Time: '+str(waitTime))
        timeLeft-=waitTime
        time.sleep(waitTime)
        
        # Do some random based keyboard movements
        # First keyboard left/right input
        leftOrRight = random.randint(0,1) #If 0 left if 1 right
        if(leftOrRight==0):
            pyautogui.keyDown('left')
            waitTime = 1+random.uniform(0,3)
            print('Time Arrow Left: '+str(waitTime))
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('left')
        else:
            pyautogui.keyDown('right')
            waitTime = 1+random.uniform(0,3)
            print('Time Arrow Right: '+str(waitTime))
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('right')
        # First keyboard left/right input end
        # Wait a small random amount of time
        waitTime = 4+random.uniform(0,5)
        print('Interval Pause Between Rotates: '+str(waitTime))
        timeLeft -= waitTime
        time.sleep(waitTime)
        #Second keyboard left/right input  
        leftOrRight = random.randint(0,1) #If 0 left if 1 right
        if(leftOrRight==0):
            pyautogui.keyDown('left')
            waitTime = 1+random.uniform(0,3)
            print('Time Arrow Left: '+str(waitTime))
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('left')
        else:
            pyautogui.keyDown('right')
            waitTime = 1+random.uniform(0,3)
            print('Time Arrow Right: '+str(waitTime))
            time.sleep(waitTime)
            timeLeft-=waitTime
            pyautogui.keyUp('right')
        #Second keyboard left/right input end
        waitTime = timeLeft+10+random.uniform(0,20)
        print('Final sleep time to wait plus a possible 30 seconds: '+str(waitTime))
        time.sleep(waitTime)
        #end wait 10+ minutes
        pyautogui.click(1492+random.randint(0,3), 51+random.randint(0,3))
        time.sleep(.5+random.uniform(0,1))
        # Reset using mouse movements and stuff, need to make more of these
        print('Start moving character to reset')
        pyautogui.click(1505, 96)
        time.sleep(6.5+random.uniform(0,1))
        pyautogui.click(1508, 118)
        time.sleep(6.5+random.uniform(0,1))
        pyautogui.click(1639, 109)
        time.sleep(6.5+random.uniform(0,1))
        pyautogui.click(1628, 144)
        time.sleep(6.5+random.uniform(0,1))
        pyautogui.click(1567, 117)
        time.sleep(6.5+random.uniform(0,1))
        print('End character reset')
except KeyboardInterrupt:
    print('Ending loop with keyboard interrupt')
