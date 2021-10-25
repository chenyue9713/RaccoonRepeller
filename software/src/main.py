import argparse
import os

from detection.run_tf_detector_batch import load_and_run_detector_batch

# model path
model_file = "/home/yue/RaccoonRepeller/software/model/md_v4.1.0.pb"
image_file = "/home/yue/RaccoonRepeller/software/images/Raccoon_1.jpg"

def process_image(file_name):
  # This runs the detector itself and tosses the output in an
  # output.json file.
  return load_and_run_detector_batch(
    model_file=model_file,
    image_file_names=[file_name],
    checkpoint_path='./output.json',
    confidence_threshold=0.85
  )

def is_animal_image(ml_result):
  for detection in ml_result['detections']:
    # A detection of '1' is an animal ('2' is a human)
    if detection['category'] == '1':
      return True
  return False

def main():

    # This is the new stuff that processes the image from
    # the camera. If the image does not contain an animal,
    # delete the image.

    ml_result = process_image(image_file)[0]
    print(ml_result)
    if is_animal_image(ml_result):
        print('Animal detected!')
    else:
        print('No animal detected')
    # os.remove(image_name)


main()