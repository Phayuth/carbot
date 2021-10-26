from __future__ import print_function
import Adafruit_BBIO.PWM as PWM
import time
import xbox

# init stick
joy = xbox.Joystick()

# assign pin PWM
Thrtpin="P8_13"
Strgpin="P9_14"

#start PWM @ 0 duty @ 50hz 
PWM.start(Thrtpin, 0, 50)
PWM.start(Strgpin, 0, 50)

try:
	thr = 0
	stg = 0
	
	while not joy.Back():
		ThrtV = joy.leftY()
		StrgV = joy.rightX()
		
		# Throttle mapping : ESC PWM arm = 6.1, Max reverse = 5.4, Max forward = 9
		if ThrtV < 0:
			thr = ((ThrtV+1)*(6.1-5.4))+5.4 # map funtion
		if ThrtV > 0:
			thr = ((ThrtV-0)*(9-6.1))+6.1 # map funtion
		
		# Steering mapping : Servo
		stg = ((StrgV+1)*(out_max-out_min)/2)+out_min
			
		PWM.set_duty_cycle(Thrtpin, thr)
		PWM.set_duty_cycle(Strgpin, stg)
		time.sleep(0.01)
	
	PWM.stop(Thrtpin)
	PWM.stop(Strgpin)
	PWM.cleanup()
	
except KeyboardInterrupt:
	print("End")
	PWM.stop(Thrtpin)
	PWM.stop(Strgpin)
	PWM.cleanup()