import numpy as np
from tqdm import tqdm
import cv2

import os
import sys

class CameraDriver(object):
    
    def __init__(self, src=0, width=640, height=480):
        self.cam = cv2.VideoCapture(src)
        self.cam.set(3,width)
        self.cam.set(4,height)

    def read(self):
        ret,frame = self.cam.read()
        return frame
    
    def update(self, frame):
        cv2.imshow('Frames',frame)
    
    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()
        


    # def start(self):
    #     if self.started:
    #         print("Camera is already started!!")
    #         return None
    #     self.started = True
