import os
import numpy as np
from PIL import Image
from skimage import color
import matplotlib.pyplot as plt
import cv2

i1 = np.array(Image.open('1.jpg'))
i2 = Image.open('2.jpg')
i3 = Image.open('3.jpg')
i4 = Image.open('4.jpg')
i5 = Image.open('5.jpg')
i6 = Image.open('6.jpg')
i7 = Image.open('7.jpg')
i8 = Image.open('8.jpg')
i9 = Image.open('9.jpg')

p1 = np.array(Image.open('1_predicted.jpg'))
p2 = Image.open('2_predicted.jpg')
p3 = Image.open('3_predicted.jpg')
p4 = Image.open('4_predicted.jpg')
p5 = Image.open('5_predicted.jpg')
p6 = Image.open('6_predicted.jpg')
p7 = Image.open('7_predicted.jpg')
p8 = Image.open('8_predicted.jpg')
p9 = Image.open('9_predicted.jpg')

g1 = np.array(Image.open('1_gray.jpg'))
g2 = np.array(Image.open('2_gray.jpg'))
g3 = np.array(Image.open('3_gray.jpg'))
g4 = np.array(Image.open('4_gray.jpg'))
g5 = np.array(Image.open('5_gray.jpg'))
g6 = np.array(Image.open('6_gray.jpg'))
g7 = np.array(Image.open('7_gray.jpg'))
g8 = np.array(Image.open('8_gray.jpg'))
g9 = np.array(Image.open('9_gray.jpg'))

fig, ax = plt.subplots(nrows=9, ncols=3)

f, a = plt.subplots(9, 3)
a[0, 0].set_title('Original')
a[0, 0].imshow(i1)
a[0, 1].set_title('Model Input')
a[0, 1].imshow(g1, cmap='gray')
a[0, 2].set_title('Prediction')
a[0, 2].imshow(p1)

a[1, 0].imshow(i2)
a[1, 1].imshow(g2, cmap='gray')
a[1, 2].imshow(p2)

a[2, 0].imshow(i3)
a[2, 1].imshow(g3, cmap='gray')
a[2, 2].imshow(p3)

a[3, 0].imshow(i4)
a[3, 1].imshow(g4, cmap='gray')
a[3, 2].imshow(p4)

a[4, 0].imshow(i5)
a[4, 1].imshow(g5, cmap='gray')
a[4, 2].imshow(p5)

a[5, 0].imshow(i6)
a[5, 1].imshow(g6, cmap='gray')
a[5, 2].imshow(p6)

a[6, 0].imshow(i7)
a[6, 1].imshow(g7, cmap='gray')
a[6, 2].imshow(p7)

a[7, 0].imshow(i8)
a[7, 1].imshow(g8, cmap='gray')
a[7, 2].imshow(p8)

a[8, 0].imshow(i9)
a[8, 1].imshow(g9, cmap='gray')
a[8, 2].imshow(p9)

for i in range(9):
    for j in range(3):
        a[i, j].axis('off')
plt.show()
