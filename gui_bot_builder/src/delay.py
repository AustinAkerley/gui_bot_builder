import time
import random

class delay(object):
	chance = 0;
	random_delay = 0;
	def __init__(self, chance, random_delay):
		self.chance = chance;
		self.random_delay = random_delay;

	def pause(self, delay_time, event):
		time.sleep(delay_time+random.uniform(0,self.random_delay));
		if(event):
			rand_event = random.randint(1,self.chance);
			sleep_time = 0;
			if(rand_event == self.chance):
				rand_type = random.randint(0,100)
				if rand_type<=70:
					sleep_time = random.randint(5,12)+random.uniform(0,1)
					print("Sleeping "+str(sleep_time)+" seconds");
					time.sleep(sleep_time);
				if rand_type>70 and rand_type<=89:
					sleep_time = random.randint(15, 45)+random.uniform(0,1)
					print("Sleeping "+str(sleep_time)+" seconds");
					time.sleep(sleep_time);
				if rand_type>89 and rand_type<98:
					sleep_time = random.randint(48,58)+random.uniform(0,1)
					print("Sleeping "+str(sleep_time)+" seconds");
					time.sleep(sleep_time);
				if rand_type >=98:
					print("This is where I'd put my logout, IF I HAD ONE!");
#BaseLine.logout();
#time.sleep(random.randint(3600, 10800)+random.uniform(0,1));
#BaseLine.login();
#time.sleep(random.randint(7,10)+random.uniform(0,1));
