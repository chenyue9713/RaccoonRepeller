from edgetpumodel import EdgeTPUModel
from tqdm import tqdm
import logging
import numpy as np



model_file = "/home/mendel/RaccoonRepeller/software/model/best1-int8.tflite"
# image_file = "/home/mendel/RaccoonRepeller/software/images/Raccoon_3.jpg"
names = "/home/mendel/RaccoonRepeller/software/images/data.yaml"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Performing test run")
n_runs = 100

model = EdgeTPUModel(model_file, names)
input_size = model.get_image_size()

inference_times = []
nms_times = []
total_times = []

for i in tqdm(range(n_runs)):
    x = (255*np.random.random((3,*input_size))).astype(np.float32)
    # print(x.shape)
    
    pred = model.forward(x)
    tinference, tnms = model.get_last_inference_time()
    
    inference_times.append(tinference)
    nms_times.append(tnms)
    total_times.append(tinference + tnms)
    
inference_times = np.array(inference_times)
nms_times = np.array(nms_times)
total_times = np.array(total_times)
    
logger.info("Inference time (EdgeTPU): {:1.2f} +- {:1.2f} ms".format(inference_times.mean()/1e-3, inference_times.std()/1e-3))
logger.info("NMS time (CPU): {:1.2f} +- {:1.2f} ms".format(nms_times.mean()/1e-3, nms_times.std()/1e-3))
fps = 1.0/total_times.mean()
logger.info("Mean FPS: {:1.2f}".format(fps))