#import cwiid
import nxt.locator
from nxt.motor import *
import time

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
robot.go()
time.sleep(1)
robot.stop()
