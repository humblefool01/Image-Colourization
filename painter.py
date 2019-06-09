import os
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
from PIL import Image, ImageEnhance
import skimage.io as io
import scipy

def grayscale(img_array, dtype='float32'):
    r, g, b = np.asarray(.3, dtype=dtype), np.asarray(.59, dtype=dtype), np.asarray(.11, dtype=dtype)
    rst = r * img_array[:, :, 0] + g * img_array[:, :, 1] + b * img_array[:, :, 2]
    rst = np.expand_dims(rst, axis=3)
    return rst

def resize(img):
    height, width = 256, 256
    img = img.resize((width, height), Image.ANTIALIAS)
    return img

def normalize(data):
    data = (data.astype(np.float32) - 127.5)/127.5
    return data

def plot_images(target, gray, prediction1):
    f, a = plt.subplots(1, 3)
    a[0].set_title('Original')
    a[0].imshow(target, interpolation='bicubic')    
    gray = np.squeeze(gray, axis=0)
    gray = np.squeeze(gray, axis=2)
    a[1].set_title('Model Input')
    a[1].imshow(gray, cmap='gray', interpolation='bicubic')
    a[2].set_title('Predicted')
    a[2].imshow(prediction1, interpolation='bicubic')
    plt.show()

print('Enter the name of the image: ')
name = input()
img_og = Image.open(str(name)+'.jpg')
w, h = img_og.size
img_og = resize(img_og)
img_a = np.array(img_og)
img_g = grayscale(img_a)
img_g = normalize(img_g)
temp = []
temp.append(img_g)
img_g = np.array(temp)
model1 = load_model('model.h5')
prediction1 = model1.predict(img_g)
prediction1 = np.squeeze(prediction1, axis=0)

scipy.misc.imsave(str(name)+'_predicted.jpg', prediction1)
img = Image.open(str(name)+'_predicted.jpg')
plot_images(img_og, img_g, img)

if w != 256 and h != 256:
    img = img.resize((w, h), Image.ANTIALIAS)
    img.save(str(name)+'_prediction_resized.jpg')
    

