import numpy as np
import time
import cv2
import pyautogui

class ScreenMatcher(object):
	"""docstring for ClassName"""
	top_left = [(0,0)];
	bottom_right = [(0,0)];
	template_path = "";
	thresh = 1;
	img = [];

	def __init__(self, template_path, thresh=0.8):
		super(ScreenMatcher, self).__init__()
		self.top_left = [];
		self.bottom_right = [];
		self.template_path = template_path;
		self.thresh = thresh;
		self.rematch();


	def rematch(self):
		# THUNK
		self.img = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB);
		# cv2.imshow('Screen', img_rgb);
		# cv2.waitKey(0);
		temp = cv2.imread(self.template_path);
		h, w, _ = temp.shape;
		res = cv2.matchTemplate(self.img, temp, cv2.TM_CCOEFF_NORMED);
		matches = np.where(res >= self.thresh);
		self.top_left= [];
		self.bottom_right = []
		for pt in zip(*matches[::-1]):
			self.top_left.append(pt);
			self.bottom_right.append((pt[0] + w, pt[1] + h));

	
	def setTemplate(self, template_path):
		self.template_path = template_path;
		self.rematch();
		for i in range(2):
			if self.top_left == []:
				time.sleep(i+1);
				self.rematch();
		if self.top_left == []:
			print "Could not find template: " + template_path;
			exit();
		


	def setThresh(self, thresh):
		self.thresh = thresh;
		self.rematch();

	def getPositions(self):
		return (self.top_left, self.bottom_right);	

	def showMatches(self):
		img_loc = self.img;
		for i in range(len(self.top_left)):
			cv2.rectangle(img_loc, self.top_left[i], self.bottom_right[i], (0, 255, 255), 2);
		cv2.imshow("Matches", img_loc);
		cv2.waitKey(0);		



if __name__ == '__main__':
	time.sleep(5);
	sm = ScreenMatcher("templates/items/flax.png");
	#print sm.getPositions()
	sm.showMatches();