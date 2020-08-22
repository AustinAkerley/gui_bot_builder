from Baseline import Baseline
from ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker
import random
import time

base = Baseline();
#nature_rune_check = ScreenMatcher("templates/items/nature_rune.png");
#astral_rune_check = ScreenMatcher("templates/items/astral_rune.png");
#coin_check = ScreenMatcher("templates/items/cash_stack");
print('Start in north edge bank with inventory of astral runes, 13 seaweed, and 13 sand buckets');
print('How much astral runes do you have: ')
#print('If you do not the bot will not stop');
astral_runes_start = input()
base.compass();

sm = ScreenMatcher("templates/interface/lunar_book.png");
mc = MatchCleaner(sm.getPositions());
cl = Clicker(chance=500);
cl.LC(mc.getCenters()[0], 1.2);
AvgProfitInv = 1.764; #assuming 3.5k per inv, spent 1736 per inventory on materials (13 seaweed 51 ea, 2 astrals 179 ea, 13 buckets sand 55 ea)
start = time.time()
Profit = 0;
astral_runes_used = 0
while astral_runes_used < astral_runes_start:
    sm.setTemplate("templates/spells/superglass_make.png");
    sm.setThresh(0.7);
    mc.setRawPos(sm.getPositions())
    cl.LC(mc.getCenters()[0], 1.4);
    astral_runes_used+=2;
    Profit+=AvgProfitInv;
    print(str(Profit) + "K made so far in "+str((time.time()-start)/60) + " minutes");

    sm.setTemplate("templates/world/grand_exchange_bank.png");
    sm.setThresh(0.7);
    mc.setRawPos(sm.getPositions())
    cl.LC(mc.getCenters()[0], 0.9);

    sm.setTemplate("templates/items/molten_glass.png");
    mc.setRawPos(sm.getPositions())
    cl.RC(mc.getCenters()[3], 0.1);

    sm.setTemplate("templates/interface/all.png");
    mc.setRawPos(sm.getPositions())
    cl.LC(mc.getCenters()[0], 0.1);

    randomPattern = random.randint(0,1)

    if(randomPattern==0):
        sm.setTemplate("templates/items/seaweed_bank.png");
        mc.setRawPos(sm.getPositions());
        cl.RC(mc.getCenters()[0], 0.1);
        sm.setTemplate("templates/interface/13.png");
        mc.setRawPos(sm.getPositions());
        cl.LC(mc.getCenters()[0], .1);
        sm.setTemplate("templates/items/bucket_sand_bank.png");
        mc.setRawPos(sm.getPositions());
        cl.RC(mc.getCenters()[0], 0.1);
        sm.setTemplate("templates/interface/13.png");
        sm.setThresh(0.9);
        mc.setRawPos(sm.getPositions());
        cl.LC(mc.getCenters()[0], 0.1);
    if(randomPattern==1):
        sm.setTemplate("templates/items/bucket_sand_bank.png");
        mc.setRawPos(sm.getPositions());
        cl.RC(mc.getCenters()[0], 0.1);
        sm.setTemplate("templates/interface/13.png");
        mc.setRawPos(sm.getPositions());
        cl.LC(mc.getCenters()[0], .1);
        sm.setTemplate("templates/items/seaweed_bank.png");
        mc.setRawPos(sm.getPositions());
        cl.RC(mc.getCenters()[0], 0.1);
        sm.setTemplate("templates/interface/13.png");
        sm.setThresh(0.9);
        mc.setRawPos(sm.getPositions());
        cl.LC(mc.getCenters()[0], 0.1);

    sm.setTemplate("templates/interface/close_bank.png");
    mc.setRawPos(sm.getPositions());
    cl.LC(mc.getCenters()[0], 0.2);
