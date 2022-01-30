from edgetpumodel import EdgeTPUModel
import cv2
import numpy as np

import os
import sys


# model path
model_file = "/home/mendel/RaccoonRepeller/software/model/best1-fp16.tflite"
image_file = "/home/mendel/RaccoonRepeller/software/images/Raccoon_3.jpg"
names = "/home/mendel/RaccoonRepeller/software/images/data.yaml"


def main():

    model = EdgeTPUModel(model_file, names)
    # input_size = model.input_size

    # model.predict(image_file)
    
    width = 640
    height = 480
    cam = cv2.VideoCapture(0)
    cam.set(3,width)
    cam.set(4,height)
    print("detect camera")

    ret,frame = cam.read()

    print(np.array(frame).shape)

    # model.predict(image_file)





main()