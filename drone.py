import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import numpy as np

yolo=YOLO()
img='0'

while img !='end':
        print('write ''end'' to Exit the loop ')
        img = input('Enter the name of image file: ')
        if img !='end':
            image = Image.open(img)
            #r_image,predicted_class,box,score = yolo.detect_image(image)
            r_image,predicted_class,predicted_score= yolo.detect_image(image)
            r_image.show()
            print(len(predicted_class))
            print(predicted_class)
            print(predicted_score)
            print(type(predicted_class))
            print(type(predicted_score))

            if len(predicted_class)>= 2:
                max_index = (predicted_score==np.max(predicted_score))
                maxElement = predicted_class[max_index]
                print(maxElement)



yolo.close_session()