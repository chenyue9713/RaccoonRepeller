from time import sleep
import queue
import sys
import signal
import time
import logging


from utilities.log import Logger


log = Logger().setup_logger('KeyBoard Controller',logging.DEBUG)

class KeyBoardController:

    def __init__(self,communication_queues):
        is_active = False

        try:

            log.debug('Starting keyBoard controller')

            signal.signal(signal.SIGINT, self.exit_gracefully)
            signal.signal(signal.SIGTERM, self.exit_gracefully)

            self._keyboard_queue = communication_queues['keyboard_controller']

            self.is_active = True

        except Exception as e:
            log.error('KeyBoard controller failed to start: {}'.format(e))
            self.is_active = False
    
    def exit_gracefully(self,signum, frame):
        log.info('Exiting keyBoard controller')
        self.is_active = False
        sys.exit(0)
    
    def do_process_events_from_queue(self):
        for x in range(0,10):
            try:
                # input_key = str(input('enter a command:'))
                input_key = 'd'
                self._keyboard_queue.put(input_key)
            except EOFError:
                return
            except Exception as e:
                log.error('KeyBoard controller failed to process events: {}'.format(e))
                self.is_active = False
                  
            


