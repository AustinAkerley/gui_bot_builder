from Baseline import Baseline
from ScreenMatcher import ScreenMatcher
from MatchCleaner import MatchCleaner
from Clicker import Clicker
import random

base = Baseline();
#nature_rune_check = ScreenMatcher("templates/items/nature_rune.png");
#astral_rune_check = ScreenMatcher("templates/items/astral_rune.png");
#coin_check = ScreenMatcher("templates/items/cash_stack");
print('Start in north edge bank with inventory of nature runes, astral runes, money, and logs.');
print('How many logs do you have: ')
#print('If you do not the bot will not stop');
num_logs = input()
base.compass();

sm3 = ScreenMatcher("templates/interface/backpack.png");
mc3 = MatchCleaner(sm3.getPositions());
cl3 = Clicker();
cl3.LC(mc3.getCenters()[0], 0.5);


sm3.setTemplate("templates/items/mahogany_log.png")
sm3.setThresh(0.7);
mc3.setRawPos(sm3.getPositions())



sm = ScreenMatcher("templates/interface/lunar_book.png");
mc = MatchCleaner(sm.getPositions());
cl = Clicker();
cl.LC(mc.getCenters()[0], 1.2);
GPPerPlank = 2147-1624

planks_made = 0
while planks_made < num_logs:
    sm2 = ScreenMatcher("templates/spells/plank_make.png");
    sm2.setThresh(0.7);
    mc2 = MatchCleaner(sm2.getPositions());
    style = random.randint(0,2)
    j=0;
    m=0;
    n=0;
    for i in range(25):
        cl.LC(mc2.getCenters()[0], .4);

        if(style==0):
            cl.LC(mc3.getCenters()[i], 0.15);
        if (style==1):
            cl.LC(mc3.getCenters()[24-i], 0.15);
        if (style==2):
            if i<7:
                cl.LC(mc3.getCenters()[i*4], 0.15);
            if 7<=i and i<13:
                cl.LC(mc3.getCenters()[3+j*4], 0.15);
                j+=1
            if 13<=i and i<19:
                cl.LC(mc3.getCenters()[2+m*4], 0.15);
                m+=1
            if 19<=i and i<25:
                cl.LC(mc3.getCenters()[1+n*4], 0.15);
                n+=1
        planks_made += 1;
    print(str(GPPerPlank*planks_made/1000)+'K profit made so far')

    sm.setTemplate("templates/world/edge_bank.png");
    sm.setThresh(0.7);
    mc.setRawPos(sm.getPositions())
    cl.LC(mc.getCenters()[0], 1);

    sm.setTemplate("templates/items/mahogany_plank.png");
    mc.setRawPos(sm.getPositions())
    cl.RC(mc.getCenters()[3], 0.5);

    sm.setTemplate("templates/interface/all.png");
    mc.setRawPos(sm.getPositions())
    cl.LC(mc.getCenters()[0], 0.5);

    sm.setTemplate("templates/items/mahogany_log_bank.png");
    mc.setRawPos(sm.getPositions());
    cl.RC(mc.getCenters()[0], 0.5);

    sm.setTemplate("templates/interface/all.png");
    mc.setRawPos(sm.getPositions());
    cl.LC(mc.getCenters()[0], 0.5);

    sm.setTemplate("templates/interface/close_bank.png");
    mc.setRawPos(sm.getPositions());
    cl.LC(mc.getCenters()[0], 0.5);
