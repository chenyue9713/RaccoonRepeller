import signal
import sys
import time
import cv2
import numpy as np
import os
import queue
import logging


from utilities.log import Logger
from camera_controller.CameraDriver import CameraDriver

log = Logger().setup_logger('Camera Controller',logging.DEBUG)


class CameraController(object):
    is_active = False


    def __init__(self, communication_queues, camera_id=0, width=640, height=480):
        try:

            log.debug('Starting camera controller')
            
            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)
            # self.cam = CameraDriver(camera_id, width, height)
            self.cam = cv2.VideoCapture(camera_id)
            self.cam.set(3,width)
            self.cam.set(4,height)
            self.ret,self.frame = self.cam.read()

            self._motion_queue = communication_queues['motion_controller']

            self.is_active = True

        except Exception as e:
            log.error('Camera controller failed to start: {}'.format(e))
            self.is_active = False
    
    def do_process_events_from_queue(self):

        try:
            while True:
                if self.is_active:
                    cv2.imshow('Frames',self.frame)
                    # cv2.imwrite('frame.jpg',self.frame)
                    self.ret,self.frame = self.cam.read()
                    
        except Exception as e:
            log.error('Camera controller failed to process events: {}'.format(e))
            self.turn_off()
            self.is_active = False
            


    def exit_gracefully(self, signum, frame):
        try:
            self.turn_off()
            log.info('Camera controller is shutting down')
        finally:
            log.info('Terminated camera controller')
            sys.exit(0)

    def turn_off(self):
        self.cam.release()
        cv2.destroyAllWindows()
        self.is_active = False


