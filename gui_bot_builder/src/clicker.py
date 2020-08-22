#!/usr/bin/python3
import pyautogui
import random
import time
from gui_bot_builder.src.delay import delay

class clicker(object):
	move_time = 0;
	hover_time = 0;
	delay = None;

	def __init__(self, move_time=.15, hover_time=.15, chance=1000, random_delay = .35):
		self.move_time = move_time;
		self.hover_time = hover_time;
		self.delay = delay(chance, random_delay);

	def left_click(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.click(position[0], position[1]);
		self.delay.pause(delay_time, event);

	def right_click(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.rightClick(position[0], position[1]);
		self.delay.pause(delay_time, event);

if __name__ == '__main__':
	my_clicky = clicker();
	my_clicky.left_click((928,345), 1.5);
	my_clicky.right_click((928,380), 3.4);
