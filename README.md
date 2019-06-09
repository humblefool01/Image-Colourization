# Image Colourization using CNN

Given a grayscale image, using convolutional neural network, it is possible to apply colour to the image. Given enough data, the CNN model can learn to predict the coloured version of the image bsaed on the content in the image. 

In this project, the model is trained to colour grayscale images of the following category:

1. People's faces
2. Coast
3. Buildings
4. Mountains
5. Forests
6. Open country 
7. Street
8. City Center


# Dataset:
+ The dataset containing people's face iamges: [CelebA dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
+ The dataset for rest of the other categories: [Computational Visual Cognition Laboratory](http://cvcl.mit.edu/database.htm)

# Model Architecture:
The model follows an encoder-decoder architecture, with skip connections from encoder fed to the decoder (U-Net). The model consists of 7 blocks of encoder followed by 7 blocks of decoder. Architecture of the model:

![flow](https://user-images.githubusercontent.com/23094225/59154892-4d6b8700-8a9a-11e9-8df5-bf9b361d9baa.png)


Each encoder block has a Convolutional layer, LeakyReLU layer followed by a BatchNormalization layer.
Each decoder block has an Addition layer to add skip connections, ConvolutionalTranspose layer, LeakyReLU layer and BatchNormalization layer.

# Results:





