import numpy as np
from tqdm import tqdm
import cv2

import os
import sys

if __name__ == "__main__" :
 
    # creating a video capture object
    # argument 0 , webcam start
    width = 640
    height = 480
    cam = cv2.VideoCapture(0)
    cam.set(3,width)
    cam.set(4,height)
    print("detect camera")

        # run a infinite loop 
    while(True) :
        try:

            # read a video frame by frame
            # read() returns tuple in which 1st item is boolean value 
            # either True or False and 2nd item is frame of the video.
            # read() returns False when live video is ended so 
            # no frame is readed and error will be generated.
            ret,frame = cam.read()
            
            # show the frame on the newly created image window
            cv2.imshow('Frames',frame)

            # this condition is used to run a frames at the interval of 10 mili sec
            # and if in b/w the frame running , any one want to stop the execution .
            if cv2.waitKey(10) & 0xFF == ord('q') :
                cv2.destroyAllWindows()
                # break out of the while loop
                break
    
        except :
            # if error occur then this block of code is run
            cv2.destroyAllWindows()
            print("Video has ended..")
            break
            
    cam.release()
    cv2.destroyAllWindows()