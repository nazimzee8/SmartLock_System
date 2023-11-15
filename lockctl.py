#lockctl.py
#Ryan Moe
#Causes servo to extend linear actuator.
#Required because Node-Red's GPIO nodes did not work for this purpose.

import RPi.GPIO as IO
import sys
import time
from numpy import interp


IO.setwarnings(False)
channel = 18
duty = 2.5

if sys.argv[1] == "lock":
    duty = 9
elif sys.argv[1] == "unlock":
    duty = 2.5
else:
    raise Exception("invalid lock state")
    print(f"USAGE: python3 {sys.argv[0]} (lock|unlock)")

IO.setmode(IO.BCM)
IO.setup(channel, IO.OUT)

pwm = IO.PWM(channel, 50)
pwm.start(duty)
time.sleep(0.5)

pwm.stop()
IO.cleanup()

print(str(int(time.time())) + f" {sys.argv[1]}ed")
#print(f"{sys.argv[1]}ed")
