from Baseline import Baseline
from ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker

mc_string = None;
base = Baseline();
sm = ScreenMatcher("templates/interface/lunar_book.png");
mc = MatchCleaner(sm.getPositions());
cl = Clicker(chance=100);

cl.LC(mc.getCenters()[0], 0.5);
base.compass();


sm.setTemplate("templates/interface/spin_flax.png");
mc.setRawPos(sm.getPositions());
for i in range(5):
		cl.LC(mc.getCenters()[0], 3);

while True:
	sm.setTemplate("templates/world/edge_bank.png");
	sm.setThresh(0.7);
	mc.setRawPos(sm.getPositions())
	cl.LC(mc.getCenters()[0], 0.5);

	
	if mc_string == None:
		sm.setTemplate("templates/items/bow_string.png");
		mc_string = MatchCleaner(sm.getPositions());
	cl.RC(mc_string.getCenters()[0], 0.2);

	sm.setTemplate("templates/interface/all.png");
	mc.setRawPos(sm.getPositions())
	cl.LC(mc.getCenters()[0], 0.2);

	sm.setTemplate("templates/items/flax.png");
	mc.setRawPos(sm.getPositions());
	cl.RC(mc.getCenters()[0], 0.2);

	sm.setTemplate("templates/interface/all.png");
	mc.setRawPos(sm.getPositions());
	cl.LC(mc.getCenters()[0], 0.2);

	sm.setTemplate("templates/interface/close_bank.png");
	mc.setRawPos(sm.getPositions());
	cl.LC(mc.getCenters()[0], 0.1);

	sm.setTemplate("templates/interface/spin_flax.png");
	mc.setRawPos(sm.getPositions());
	for i in range(5):
		cl.LC(mc.getCenters()[0], 3);


	

	

	

	
	
	
	
