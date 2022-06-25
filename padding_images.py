import os

import cv2
import numpy as np
import os
from PIL import Image

base_path = 'D:\\TSLT\\PyCharm\\Yolo5\\runs\\detect\\exp\\crops\\'

def createFolder(crops, sub_folder):
       nameFolder = 'padding_'+sub_folder
       pading_folder = crops+nameFolder
       try:
              os.mkdir(pading_folder)

              print("Directory", nameFolder, "Created")
       except FileExistsError:
              print("Directory", nameFolder, "already exists")
       return pading_folder+'\\'


def padding(old_image_width, old_image_height, new_image_width, new_image_height):
       x_center = (new_image_width - old_image_width) // 2
       y_center = (new_image_height - old_image_height) // 2
       return x_center, y_center



for folderName in os.listdir((base_path)):
       if folderName[0] == 'D':
              path_of_the_directory = base_path + folderName + '\\'
              # print(path_of_the_directory)
              for sub_folder in os.listdir(path_of_the_directory):
                     if (sub_folder != '.DS_Store') and (sub_folder != 'desktop.ini'):
                            #print(sub_folder)
                            crops = path_of_the_directory + sub_folder + '\\Humand hand\\'
                           # print(crops)
                            pading_folder = createFolder(crops, sub_folder)


                            for (root, dirs, file) in os.walk(crops):
                                   for images in file:
                                          frames = Image.open(crops+images)
                                          # get width and height
                                          print(crops+images, ' = ', frames.size)

                                          # read image
                                          img = cv2.imread(crops+images)
                                          old_image_height, old_image_width, channels = img.shape
                                          print(old_image_width, old_image_height, channels)

                                          # create new image of desired size and color (blue) for padding
                                          new_image_width = 224
                                          new_image_height = 224
                                          new_size = (new_image_width,new_image_height)
                                          color = (255,255,255)
                                          result = np.full((new_image_height, new_image_width, channels), color,dtype=np.uint8)


                                          if (old_image_width < new_image_width) and (old_image_height < new_image_height) :
                                                 print('case = 1')
                                                 # # copy img image into center of result image
                                                 x_center, y_center = padding(old_image_width, old_image_height,new_image_width, new_image_height)
                                                 result[y_center:y_center + old_image_height,
                                                 x_center:x_center + old_image_width] = img
                                                 cv2.imwrite(pading_folder+images, result)
                                                 print(result.shape)

                                          elif (old_image_width > new_image_width) and (old_image_height < new_image_height) :
                                                 print('case 2')
                                                 x_resize = cv2.resize(img, (new_image_width, old_image_height))
                                                 print(x_resize.shape[1], x_resize.shape[0])
                                             #    cv2.imwrite("case2_resize.jpg", x_resize)

                                                 old_image_height, old_image_width, channels = x_resize.shape

                                                 # compute center offset
                                                 x_center, y_center = padding(old_image_width, old_image_height,
                                                                              new_image_width, new_image_height)

                                                 result[y_center:y_center + old_image_height,
                                                 x_center:x_center + old_image_width] = x_resize

                                                 cv2.imwrite(pading_folder+images, result)
                                                 print(result.shape)

                                          elif (old_image_width < new_image_width) and (old_image_height > new_image_height) :
                                                 print('case 3')
                                                 y_resize = cv2.resize(img, (old_image_width, new_image_height))
                                                 print(y_resize.shape[1], y_resize.shape[0])
                                              #   cv2.imwrite("case3_resize.jpg", y_resize)

                                                 old_image_height, old_image_width, channels = y_resize.shape

                                                 # compute center offset
                                                 x_center, y_center = padding(old_image_width, old_image_height,
                                                                              new_image_width, new_image_height)

                                                 result[y_center:y_center + old_image_height,
                                                 x_center:x_center + old_image_width] = y_resize

                                                 cv2.imwrite(pading_folder+images, result)
                                                 print(result.shape)
                                          else:
                                                 print('case 4')
                                                 xy_resize = cv2.resize(img, (new_image_width, new_image_height))
                                                 cv2.imwrite(pading_folder+images, xy_resize)
                                                 print(xy_resize.shape)

