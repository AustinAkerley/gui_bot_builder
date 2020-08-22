from Baseline import Baseline
from ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker

base = Baseline();
base.setPassword("aa212692");
base.login();
sm = ScreenMatcher("templates/interface/lunar_book.png");



mc = MatchCleaner(sm.getPositions());
cl = Clicker();
cl.LC(mc.getCenters()[0], 0.5);
base.compass();

sm.setTemplate("templates/interface/spin_flax.png");
mc.setRawPos(sm.getPositions());
for i in range(5):
		cl.LC(mc.getCenters()[0], 3);

while True:
	sm.setTemplate("templates/world/edge_bank.png");
	mc.setRawPos(sm.getPositions())
	cl.LC(mc.getCenters()[0], 1);

	sm.setTemplate("templates/items/bow_string.png");
	mc.setRawPos(sm.getPositions())
	cl.RC(mc.getCenters()[3], 0.5);

	sm.setTemplate("templates/interface/all.png");
	mc.setRawPos(sm.getPositions())
	cl.LC(mc.getCenters()[0], 0.5);

	sm.setTemplate("templates/items/flax.png");
	mc.setRawPos(sm.getPositions());
	cl.RC(mc.getCenters()[0], 0.5);

	sm.setTemplate("templates/interface/all.png");
	mc.setRawPos(sm.getPositions());
	cl.LC(mc.getCenters()[0], 0.5);

	sm.setTemplate("templates/interface/close_bank.png");
	mc.setRawPos(sm.getPositions());
	cl.LC(mc.getCenters()[0], 0.5);

	sm.setTemplate("templates/interface/spin_flax.png");
	mc.setRawPos(sm.getPositions());
	for i in range(5):
		cl.LC(mc.getCenters()[0], 3);


	

	

	

	
	
	
	