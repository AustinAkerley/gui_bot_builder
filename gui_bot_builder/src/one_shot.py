# Title: Random Large Delay to Simulate Human Behavior
# Creator: Austin Akerley
# Date Created: 08/22/2020
# Last Editor: Austin Akerely
# Date Last Edited: 08/22/2020

# INPUT(s) -
# chance - type: int, desc: This is probability that the long delay will happen % [100*(1/chance)]
# time - type: float, desc: This is how long you want it to wait if it happens to trigger the delay
# random_delay - type: float, desc: This is the random component in the delay if the delay is indeed triggered

import random
from gui_bot_builder.src.delay import delay

def one_shot(chance, delay_time, random_delay):
    trigger = random.randint(1,chance)
    test = 1
    if trigger == test:
        print("Executing long humanized delay for: "+str(delay_time) + " to " +str(delay_time+random_delay) + " seconds.")
        delay(delay_time, random_delay)
