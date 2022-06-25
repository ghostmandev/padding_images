import os

import cv2
import numpy as np
import os
from PIL import Image

base_path = 'D:\\TSLT\\PyCharm\\crop_test\\'



for folderName in os.listdir((base_path)):
       if folderName[0] == 'D':
              path_of_the_directory = base_path + folderName + '\\'
              # print(path_of_the_directory)
              for sub_folder in os.listdir(path_of_the_directory):
                     if (sub_folder != '.DS_Store') and (sub_folder != 'desktop.ini'):
                            #print(sub_folder)
                            crops = path_of_the_directory + sub_folder + '\\Humand hand\\'
                           # print(crops)
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
                                          color = (255,255,255)
                                          if (old_image_width < new_image_width) and (old_image_height < new_image_height) :
                                                 print('loop = 1')
                                                 result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

                                                 # compute center offset
                                                 x_center = (new_image_width - old_image_width) // 2
                                                 y_center = (new_image_height - old_image_height) // 2

                                                 # copy img image into center of result image

                                                 result[y_center:y_center+old_image_height, x_center:x_center + old_image_width] = img

                                          elif (old_image_width > new_image_width) and (old_image_height < new_image_height) :
                                                 print('loop = 2')
                                                 result = np.full((new_image_height, new_image_width, channels), color,dtype=np.uint8)

                                                 x_center = (new_image_width - old_image_width) // 2
                                                 y_center = (new_image_height - old_image_height) // 2

                                                 result[y_center:y_center + old_image_height,
                                                 x_center:x_center + old_image_width] = img

                                          elif (old_image_width < new_image_width) and (old_image_height > new_image_height) :
                                                 print('loop = 3')
                                                 result = np.full((new_image_height, new_image_width, channels), color,dtype=np.uint8)

                                                 x_center = (new_image_width - old_image_width) // 2
                                                 y_center = (new_image_height - old_image_height) // 2

                                                 result[y_center:y_center+old_image_height, x_center:x_center + old_image_width] = img

                                          else :
                                                 print('loop = 4')
                                                 x_new_resize = old_image_width.resize(new_image_width)
                                                 y_new_resize = old_image_height.resize(new_image_height)
                                                 result[x_new_resize, y_new_resize] = img





                                          # # view result
                                          # cv2.imshow("result", result)
                                          # cv2.waitKey(0)
                                          # cv2.destroyAllWindows()

                                          # save result
                                          print(result.shape)
                                          cv2.imwrite("lena_centered.jpg", result)







