#import cwiid
import nxt.locator
from nxt.motor import *
<<<<<<< HEAD
=======
import time
>>>>>>> 0f956f51b496154c3dd7a089c70f6c631a441e46

class NXT:
    def __init__(self):
        b = nxt.locator.find_one_brick()
        self.m_left = Motor(b, PORT_B)
        self.m_right = Motor(b,PORT_C)

    def go(self):
        self.m_left.run()
        self.m_right.run()

    def stop(self):
        self.m_left.brake()
        self.m_right.brake()

robot = NXT()
<<<<<<< HEAD
=======
robot.go()
time.sleep(1)
robot.stop()
>>>>>>> 0f956f51b496154c3dd7a089c70f6c631a441e46
