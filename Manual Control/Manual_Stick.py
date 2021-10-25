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
    dc = 0
    StrgV = 0
    
    while not joy.Back():
        ThrtV = joy.leftY()
        StrgV = joy.rightX()
        
        if ThrtV < 0:
            dc = ((ThrtV+1)*(6.1-5.4))+5.4 # map funtion
        if ThrtV > 0:
            dc = ((ThrtV-0)*(9-6.1))+6.1 # map funtion
        
        #ESC PWM arm = 6.1, Max reverse = 5.4, Max forward = 9
        if dc <5.4:
            dc = 5.4
        if dc > 9:
            dc = 9
            
        PWM.set_duty_cycle(Thrtpin, dc)
        PWM.set_duty_cycle(Strgpin, abs(StrgV)*10)
        time.sleep(0.01)
    
    PWM.stop(Thrtpin)
    PWM.stop(Strgpin)
    PWM.cleanup()
    
except KeyboardInterrupt:
    print("End")
    PWM.stop(Thrtpin)
    PWM.stop(Strgpin)
    PWM.cleanup()