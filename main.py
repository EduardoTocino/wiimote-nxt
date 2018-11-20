#import cwiid
import nxt.locator
from nxt.motor import *

class NXT:
    def __init__(self):
        print("Connecting to NXT...")
        try:
            b = nxt.locator.find_one_brick()
        except nxt.locator.BrickNotFoundError as error:
            print("NXT not found.")
            exit()
        print("Connected!")
        self.m_left = Motor(b, PORT_B)
        self.m_right = Motor(b,PORT_C)

    def go(self):
        self.m_left.run()
        self.m_right.run()

    def stop(self):
        self.m_left.brake()
        self.m_right.brake()

robot = NXT()
