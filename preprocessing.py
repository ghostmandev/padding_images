import numpy as np
from PIL import Image
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import pickle

base_path = 'D:\\TSLT\\PyCharm\\Yolo5\\runs\\detect\\exp\\crops\\'
countFrames = 0
count = 0
photos, labels, datas = list(), list(), list()
for folderName in os.listdir((base_path)):
       if folderName[0] == 'D':
              path_of_the_directory = base_path + folderName + '\\'
              # print(path_of_the_directory)
              for sub_folder in os.listdir(path_of_the_directory):
                     if (sub_folder != '.DS_Store') and (sub_folder != 'desktop.ini'):
                            # print(sub_folder)
                            crops = path_of_the_directory + sub_folder + '\\Humand hand\\'
                            for crop_folder in os.listdir(crops):
                                   if crop_folder[:3] == 'pad' :
                                          crop_path = crops+crop_folder
                                          for root, dirs, files in os.walk(crop_path):
                                                 for images in files:
                                                        count += 1
                                                        images_path = crop_path +'\\' +images
                                                        frames = Image.open(images_path)
                                                        countFrames += 1
                                                        # get width and height
                                                       # print(images_path, ' = ', frames.size)

                                                        photo = load_img(images_path, target_size=(224,224))
                                                        photo = img_to_array(photo)

                                                        photos = np.append(photos, photo)
                                                        datas = photos.reshape(count,224,224,3)
                                                        labels = np.append(labels,sub_folder)
                                                 print(datas.shape, labels.shape)

print('All Frames = ', countFrames )

pre_data = datas
f = open('cnn_ma_crop_data_260622_1_to_9_(224x224).pkl','wb')
pickle.dump(pre_data,f)
f.close()

pre_labels = labels
g = open('cnn_ma_crop_labels_260622_1_to_9_(224x224).pkl','wb')
pickle.dump(pre_labels, g)
g.close()