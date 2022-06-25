import cv2
import numpy as np
from PIL import Image

# read image
img = cv2.imread('case4.jpg')
old_image_height, old_image_width, channels = img.shape
print(old_image_width, old_image_height)
# create new image of desired size and color (blue) for padding
new_image_width = 224
new_image_height = 224
color = (255,255,255)
result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)
if old_image_width < new_image_width and old_image_height < new_image_height:
       print('case 1')


       # compute center offset
       x_center = (new_image_width - old_image_width) // 2
       y_center = (new_image_height - old_image_height) // 2

       # copy img image into center of result image
       result[y_center:y_center+old_image_height,x_center:x_center+old_image_width] = img
       cv2.imwrite("case1_final.jpg", result)
       print(result.shape)

elif old_image_width > new_image_width and old_image_height < new_image_height:
       print('case 2')
       x_resize = cv2.resize(img, (new_image_width, old_image_height))
       print(x_resize.shape[1], x_resize.shape[0])
       cv2.imwrite("case2_resize.jpg", x_resize)

       old_image_height, old_image_width, channels = x_resize.shape
       # print(old_image_width, old_image_height)

       # compute center offset
       x_center = (new_image_width - old_image_width) // 2
       y_center = (new_image_height - old_image_height) // 2

       result[y_center:y_center + old_image_height, x_center:x_center + old_image_width] = x_resize

       cv2.imwrite("case2_final.jpg", result)
       print(result.shape)


elif old_image_width < new_image_width and old_image_height > new_image_height:
       print('case 3')
       y_resize = cv2.resize(img, (old_image_width, new_image_height))
       print(y_resize.shape[1], y_resize.shape[0])
       cv2.imwrite("case3_resize.jpg", y_resize)


       old_image_height, old_image_width, channels = y_resize.shape
       # print(old_image_width, old_image_height)

       # compute center offset
       x_center = (new_image_width - old_image_width) // 2
       y_center = (new_image_height - old_image_height) // 2

       result[y_center:y_center + old_image_height, x_center:x_center + old_image_width] = y_resize

       cv2.imwrite("case3_final.jpg", result)
       print(result.shape)

else:
       print('case 4')
       xy_resize = cv2.resize(img,(new_image_width, new_image_height))
       cv2.imwrite("case4_final.jpg", xy_resize)
       print(xy_resize.shape)
       # print(xy_resize.widht, xy_resize.height)


# # view result
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# save result
#cv2.imwrite("1-19_final.jpg", y_resize)