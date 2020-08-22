import pyautogui
import random
import time
def usePots(potsUsedThusFar):
    if potsUsedThusFar<4:
        print('Clciking first pots')
        pyautogui.click(1466, 761)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1508, 764)
    if 4 <= potsUsedThusFar < 8:
        print('Clciking second pots')
        pyautogui.click(1550, 762)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1595, 761)
    if 8 <= potsUsedThusFar < 12:
        print('Clciking third pots')
        pyautogui.click(1466, 799)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1509, 797)
    if 12 <= potsUsedThusFar < 16:
        print('Clciking fourth pots')
        pyautogui.click(1551, 799)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1592, 800)
    if 16 <= potsUsedThusFar < 20:
        print('Clciking fith pots')
        pyautogui.click(1468, 836)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1508, 837)
    if 20 <= potsUsedThusFar < 24:
        print('Clciking sixth pots')
        pyautogui.click(1548, 838)
        time.sleep(1.6+random.uniform(0,1))
        pyautogui.click(1592, 835)
    #if 24 <= potsUsedThusFar < 28:
        #print('Clciking seventh pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
    #if 28 <= potsUsedThusFar < 32:
        #print('Clciking eighth pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
    #if 32 <= potsUsedThusFar < 36:
        #print('Clciking nineth pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
    #if 36 <= potsUsedThusFar < 40:
        #print('Clciking tenth pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
    #if 40 <= potsUsedThusFar < 44:
        #print('Clciking eleventh pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
    #if 44 <= potsUsedThusFar < 48:
        #print('Clciking twelth pots')
        #pyautogui.click()
        #time.sleep(1.6+random.uniform(0,1))
        #pyautogui.click()
        
print ('What row is your STR and ATT pots on: ')
potsRow = input()
potsRow-=1
print('Skip to using pots stage(0 yes, 1 no): ')
skipToPots=input()
potsUsed = potsRow*8
width, height = pyautogui.size()
# Set time variable (a.k.a. time that this program should run)
timeOperational = 4 #in hours
i=0
timeLeft = 0
# Begin Loop
try:
    while i <= 6*timeOperational :
        if(skipToPots==1):
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
        skipToPots=1
        time.sleep(3)
        print('Pots Used: '+str(potsUsed))
        usePots(potsUsed)
        potsUsed+=1
        waitTime = timeLeft+random.uniform(0,8)
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
        print('End character reset\n\n')
        i+=1
except KeyboardInterrupt:
    print('Ending loop with keyboard interrupt')
