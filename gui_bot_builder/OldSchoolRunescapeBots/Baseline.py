from gui_bot_builder.ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker
import pyautogui
import time

class Baseline(object):
	"""docstring for Baseline"""
	sm = None;
	mc = None;
	cl = None;
	password = "";

	def __init__(self):
		super(Baseline, self).__init__()

	def setPassword(self, password):
		self.password = password;

	def login(self):
		sm = ScreenMatcher("templates/login/existing.png");
		mc = MatchCleaner(sm.getPositions());
		cl = Clicker();
		cl.LC(mc.getCenters()[0], 0.5);
		pyautogui.typewrite(self.password, interval=0.1);
		sm = ScreenMatcher("templates/login/login.png");
		mc = MatchCleaner(sm.getPositions());
		#print(mc.getCenters());
		cl.LC(mc.getCenters()[0], 5);

		sm = ScreenMatcher("templates/login/play.png");
		mc = MatchCleaner(sm.getPositions());
		cl.LC(mc.getCenters()[0], 0.5);
		# reset screen from logout call

	def compass(self):
		sm = ScreenMatcher("templates/interface/compass.png", 0.6);
		mc = MatchCleaner(sm.getPositions());
		cl = Clicker();
		cl.LC(mc.getCenters()[0], 0.5);
		pyautogui.keyDown('up');
		time.sleep(1.9);
		pyautogui.keyUp('up');



if __name__ == '__main__':
	base = Baseline();
	base.compass()
