# from edgetpumodel import EdgeTPUModel
# import cv2
# import numpy as np
from camera_controller.camera_controller import CameraController
from motion_controller.motion_controller import MotionController
from keyBoard_controller.keyBoard_controller import KeyBoardController
from utilities.log import Logger

import multiprocessing

import os
import sys
import logging


log = Logger().setup_logger()

# model path
# model_file = "/home/mendel/RaccoonRepeller/software/model/best1-fp16.tflite"
# image_file = "/home/mendel/RaccoonRepeller/software/images/Raccoon_3.jpg"
# names = "/home/mendel/RaccoonRepeller/software/images/data.yaml"


# Controller queues
def create_controllers_queues():
    communication_queues = {'camera_controller': multiprocessing.Queue(10),
                            'motion_controller': multiprocessing.Queue(10),
                            'keyboard_controller': multiprocessing.Queue(10)}

    log.info('Created the communication queues: ' + ', '.join(communication_queues.keys()))

    return communication_queues

    
def process_camera_controller(communication_queues):
    # Camera controller
    camera_controller = CameraController(communication_queues)
    camera_controller.do_process_events_from_queue()

def process_motion_controller(communication_queues):
    # Motion controller
    motion_controller = MotionController(communication_queues)
    motion_controller.do_process_events_from_queue()

def process_keyboard_controller(communication_queues):
    # Keyboard controller
    keyboard_controller = KeyBoardController(communication_queues)
    keyboard_controller.do_process_events_from_queue()

def close_controllers_queues(communication_queues):
    log.info('Closing controllers queues')

    for queue in communication_queues.items():
        queue.close()
        queue.join_thread()



def main():
    communication_queues = create_controllers_queues()
    
    # Camera controller process
    camera_process = multiprocessing.Process(target=process_camera_controller, args=(communication_queues,))
    camera_process.daemon = True

    # Motion controller process
    motion_process = multiprocessing.Process(target=process_motion_controller, args=(communication_queues,))
    motion_process.daemon = True

    # Keyboard controller process
    keyboard_process = multiprocessing.Process(target=process_keyboard_controller, args=(communication_queues,))
    keyboard_process.daemon = True

    # Start processes, queues messages are produced and consumed
    camera_process.start()
    motion_process.start()
    keyboard_process.start()

    if not camera_process.is_alive():
        log.error('Camera controller failed to start')
        sys.exit(1)
    
    if not motion_process.is_alive():
        log.error('Motion controller failed to start')
        sys.exit(1)

    if not keyboard_process.is_alive():
        log.error('Keyboard controller failed to start')
        sys.exit(1)

    # Wait for the controllers to finish
    camera_process.join()
    motion_process.join()
    keyboard_process.join()

    close_controllers_queues(communication_queues)


if __name__ == '__main__':
    log.info('Raccoon Repeller is starting')

    try:
        main()

    except KeyboardInterrupt:
        log.info('Terminated due Control+C was pressed')

    else:
        log.info('Raccoon Repeller is shutting down')






    # model = EdgeTPUModel(model_file, names)
    # # input_size = model.input_size

    # # model.predict(image_file)
    
    # width = 640
    # height = 480
    # cam = cv2.VideoCapture(0)
    # cam.set(3,width)
    # cam.set(4,height)
    # print("detect camera")

    # ret,frame = cam.read()

    # print(np.array(frame).shape)

    # model.predict(image_file)
