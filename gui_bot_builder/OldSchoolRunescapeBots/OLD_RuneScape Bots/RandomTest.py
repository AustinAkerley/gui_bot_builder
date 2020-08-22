import pyautogui
import random
import time

def usePots(potsUsedThusFar):
    if potsUsedThusFar<4:
        print('Clciking first pots')
        pyautogui.click(1466, 761)
        time.sleep(1.6)
        pyautogui.click(1508, 764)
    if 4 <= potsUsedThusFar < 8:
        print('Clciking second pots')
        pyautogui.click(1550, 762)
        time.sleep(1.6)
        pyautogui.click(1595, 761)
    if 8 <= potsUsedThusFar < 12:
        print('Clciking third pots')
        pyautogui.click(1466, 799)
        time.sleep(1.6)
        pyautogui.click(1509, 797)
    if 12 <= potsUsedThusFar < 16:
        print('Clciking fourth pots')
        pyautogui.click(1551, 799)
        time.sleep(1.6)
        pyautogui.click(1592, 800)
    if 16 <= potsUsedThusFar < 20:
        print('Clciking fith pots')
        pyautogui.click(1468, 836)
        time.sleep(1.6)
        pyautogui.click(1508, 837)
    if 20 <= potsUsedThusFar < 24:
        print('Clciking sixth pots')
        pyautogui.click(1548, 838)
        time.sleep(1.6)
        pyautogui.click(1592, 835)
    if 24 <= potsUsedThusFar < 28:
        print('Clciking seventh pots')
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()
    if 28 <= potsUsedThusFar < 32:
        print('Clciking eighth pots')
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()
    if 32 <= potsUsedThusFar < 36:
        print('Clciking first pots')
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()
    if 36 <= potsUsedThusFar < 40:
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()
    if 40 <= potsUsedThusFar < 44:
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()
    if 44 <= potsUsedThusFar < 48:
        pyautogui.click()
        time.sleep(1.6)
        pyautogui.click()

potsUsed = 4
usePots(potsUsed)
