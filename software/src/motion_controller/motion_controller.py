from periphery import GPIO
from time import sleep
import queue
import sys
import signal
import time
import logging


from utilities.log import Logger


log = Logger().setup_logger('Motion Controller',logging.DEBUG)

class MotionController:
    is_active = False
    is_auto = False

    base_motor_direction = None
    base_motor_step = None
    base_motor_cw = True # Clockwise Rotation
    base_motor_ccw = False # Counterclockwise Rotation
    base_motor_spr = None 
    base_motor_step_count = None

    arm_motor_direction = None
    arm_motor_step = None
    arm_motor_cw = True # Clockwise Rotation
    arm_motor_ccw = False # Counterclockwise Rotation
    arm_motor_spr = None 

    arm_motor_step_count = None

    delay = None

    def __init__(self,communication_queues):

        try:
                
            log.debug('Starting motion controller')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            self.base_motor_direction = GPIO("/dev/gpiochip0", 7, "out")
            self.base_motor_step = GPIO("/dev/gpiochip0", 8, "out")
            self.base_motor_spr = 2 # Steps per Revolution (360 / 7.5)

            self.arm_motor_direction = GPIO("/dev/gpiochip2", 9, "out")
            self.arm_motor_step = GPIO("/dev/gpiochip4", 10, "out")
            self.arm_motor_spr = 2 # Steps per Revolution (360 / 7.5)

            self.base_motor_step_count = self.base_motor_spr
            self.arm_motor_step_count = self.arm_motor_spr

            self.delay = .0005

            # self._motion_queue = communication_queues['motion_controller']
            self._keyboard_queue = communication_queues['keyboard_controller']
            

            self.is_active = True
        
        except Exception as e:
            log.error('Error in motion controller: {}'.format(e))
            try:
                log.info('Exiting motion controller')
                self.base_motor_direction.close()
                self.base_motor_step.close()
                self.arm_motor_direction.close()
                self.arm_motor_step.close()
            finally:
                log.info('Terminated motion controller')
                sys.exit(1)

    def exit_gracefully(self,signum, frame):
        log.info('Exiting motion controller')
        try:
            self.base_motor_direction.close()
            self.base_motor_step.close()
            self.arm_motor_direction.close()
            self.arm_motor_step.close()
        finally:
            log.info('Terminated motion controller')
            sys.exit(1)

    def do_process_events_from_queue(self):
        while self.is_active:
            try:
                if self.is_auto:

                    event = self._motion_queue.get(block=True, timeout=None)
                    pass

                else:
                    # pass
                    event = self._keyboard_queue.get(block=True, timeout=60)
                    log.debug('Keyboard event: {}'.format(event))

                    if event == 'h':
                        # add home position, press s will move to home position
                        pass
                    if event == 'w':
                        # camera up
                        self.arm_motor_direction.write(self.arm_motor_cw)
                        for x in range(self.arm_motor_step_count):
                            self.arm_motor_step.write(True)
                            sleep(self.delay)
                            self.arm_motor_step.write(False)
                            sleep(self.delay)
                        pass
                    if event == 's':
                        # camera down
                        self.arm_motor_direction.write(self.arm_motor_ccw)
                        for x in range(self.arm_motor_step_count):
                            self.arm_motor_step.write(True)
                            sleep(self.delay)
                            self.arm_motor_step.write(False)
                            sleep(self.delay)
                        pass
                    if event == 'a':
                        # camera left
                        self.base_motor_direction.write(self.base_motor_ccw)
                        for x in range(self.base_motor_step_count):
                            self.base_motor_step.write(True)
                            sleep(self.delay)
                            self.base_motor_step.write(False)
                            sleep(self.delay)
                        pass
                    if event == 'd':
                        # camera right
                        self.base_motor_direction.write(self.base_motor_cw)
                        for x in range(self.base_motor_step_count):
                            self.base_motor_step.write(True)
                            sleep(self.delay)
                            self.base_motor_step.write(False)
                            sleep(self.delay)
                        pass
            # Add queue except for motion controller later            
            except queue.Empty as e:
                log.info('Didnt get input from KeyBoard lated 60 seconds,'
                        'please press a key or exit')
                
            except Exception as e:
                log.error('Error in motion controller: {}'.format(e))

            
                      
                    

                

                

    

    