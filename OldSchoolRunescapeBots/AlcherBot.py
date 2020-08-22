from Baseline import Baseline
from ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker
import time

alch_count = 0;
base = Baseline();
cl = Clicker(chance=100, random_delay=.7);
sm = ScreenMatcher("templates/interface/normal_book.png");
mc = MatchCleaner(sm.getPositions());
cl.LC(mc.getCenters()[0], .5);

sm.setTemplate("templates/spells/high_alch.png");
while True:
	print "Alched %i times so far." % alch_count;
	mc.setRawPos(sm.getPositions());
	cl.LC(mc.getCenters()[0], 0);

	sm.setTemplate("templates/bot_specific/alcher/cast.png");
	if not sm.getPositions()[0] == []:
		cl.LC(mc.getCenters()[0], 0.3)
	else:
		sm.setTemplate("templates/items/rune_arrows.png");
		mc.setRawPos(sm.getPositions());
		cl.LC(mc.getCenters()[0], 0.3);
	alch_count += 1;

	count = 0;
	sm.setTemplate("templates/spells/high_alch.png");
	while sm.getPositions()[0] == [] and count < 100:
		time.sleep(0.3);
		sm.rematch();
		count += 1;
	if count == 100:
		exit();

	print '\n';
