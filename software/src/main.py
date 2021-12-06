from edgetpumodel import EdgeTPUModel

# model path
model_file = "/home/mendel/RaccoonRepeller/software/model/best1-fp16.tflite"
image_file = "/home/mendel/RaccoonRepeller/software/images/Raccoon_3.jpg"
names = "/home/mendel/RaccoonRepeller/software/images/data.yaml"


def main():

    model = EdgeTPUModel(model_file, names)

    model.predict(image_file)


main()