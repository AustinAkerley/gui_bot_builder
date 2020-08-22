# Title: Delay
# Creator: Austin Akerley
# Date Created: 08/22/2020
# Last Editor: Austin Akerely
# Date Last Edited: 08/22/2020

import time
import random

# INPUT(s) -
# time - type: float, desc: the amount of time in seconds you wish for the base delay
# random_delay - type: float, desc: The amount of random delay, 1.0 is suggested

def delay(delay_time, random_delay = 0): # 0 random delay for no random delay
	sleep_time = delay_time + random.uniform(0, random_delay)
	print("Sleeping for: "+str(sleep_time) + " seconds.")
	time.sleep(sleep_time)
