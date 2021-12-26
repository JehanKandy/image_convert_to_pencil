import numpy as np
import imageio
import scipy.ndimage
import cv2


my_img = "my_photo.jpg"
def rgb_photo(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])


def image(frant, back):
    final_sketch = frant*255/(255-back)
    final_sketch[final_sketch>255] = 255
    final_sketch[back==255]=255
    
    return final_sketch.astype('uint8')

img = imageio.imread(my_img)

gray = rgb_photo(img)

g = 255-gray

blur = scipy.ndimage.filters.gaussian_filter(g, sigma =15)

f_image = image(blur, gray)

cv2.imwrite('final_image.png', f_image)
