import pyautogui
import random
import time
from Delay import Delay

class Clicker(object):
	move_time = 0;
	hover_time = 0;
	delay = None;

	def __init__(self, move_time=.15, hover_time=.15, chance=1000, random_delay = .35):
		self.move_time = move_time;
		self.hover_time = hover_time;
		self.delay = Delay(chance, random_delay);

	def LC(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.click(position[0], position[1]);
		self.delay.pause(delay_time, event);

	def RC(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.rightClick(position[0], position[1]);
		self.delay.pause(delay_time, event);

if __name__ == '__main__':
	myClicky = Clicker();
	myClicky.LC((928,345), 1.5);
	myClicky.LC((928,380), 3.4);