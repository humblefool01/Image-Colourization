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
The model follows an encoder-decoder architecture, with skip connections from encoder fed to the decoder (U-Net). The model consists of 7 blocks of encoder followed by 7 blocks of decoder. Each encoder block has a Convolutional layer, LeakyReLU layer followed by a BatchNormalization layer and Dropout layer.
Each decoder block has an Addition layer to add skip connections, ConvolutionalTranspose layer, LeakyReLU layer and BatchNormalization layer. Architecture of the model:

![flow](https://user-images.githubusercontent.com/23094225/59154892-4d6b8700-8a9a-11e9-8df5-bf9b361d9baa.png)


# Results:

## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ground Truth &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Model Input &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Model Output

![1](https://user-images.githubusercontent.com/23094225/59155636-af80b800-8aab-11e9-954a-156de3b73475.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![1_gray](https://user-images.githubusercontent.com/23094225/59155642-ee167280-8aab-11e9-8bd1-aa1ab25171dc.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![1_predicted](https://user-images.githubusercontent.com/23094225/59155646-1900c680-8aac-11e9-921e-302668913378.jpg)

![2](https://user-images.githubusercontent.com/23094225/59155662-a6dcb180-8aac-11e9-9146-d204684f3478.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![2_gray](https://user-images.githubusercontent.com/23094225/59155667-b5c36400-8aac-11e9-82f4-4ca362824add.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![2_predicted](https://user-images.githubusercontent.com/23094225/59155669-c1af2600-8aac-11e9-9351-d7242319c03a.jpg)

![3](https://user-images.githubusercontent.com/23094225/59155672-d7245000-8aac-11e9-8518-e3d2bc233754.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![3_gray](https://user-images.githubusercontent.com/23094225/59155683-ffac4a00-8aac-11e9-81cd-aba2656e4852.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![3_predicted](https://user-images.githubusercontent.com/23094225/59155688-0a66df00-8aad-11e9-9805-11ebada5ed8e.jpg)

![4](https://user-images.githubusercontent.com/23094225/59155700-33876f80-8aad-11e9-912d-c863e9821ae0.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![4_gray](https://user-images.githubusercontent.com/23094225/59155705-3eda9b00-8aad-11e9-938f-c4dd749717a8.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![4_predicted](https://user-images.githubusercontent.com/23094225/59155709-4c902080-8aad-11e9-8d9f-432dd6e9912f.jpg)

![5](https://user-images.githubusercontent.com/23094225/59155713-603b8700-8aad-11e9-9ba4-d7f525b1ac88.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![5_gray](https://user-images.githubusercontent.com/23094225/59155714-6af61c00-8aad-11e9-9800-9c8f7d769427.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![5_predicted](https://user-images.githubusercontent.com/23094225/59155715-75b0b100-8aad-11e9-9e8f-75ce5d4fec20.jpg)

![6](https://user-images.githubusercontent.com/23094225/59155720-8cef9e80-8aad-11e9-905f-f7dcb6355975.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![6_gray](https://user-images.githubusercontent.com/23094225/59155724-96790680-8aad-11e9-88d2-37923abf4d77.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![6_predicted](https://user-images.githubusercontent.com/23094225/59155726-a264c880-8aad-11e9-8900-6b6ca413d61b.jpg)

![7](https://user-images.githubusercontent.com/23094225/59155730-b6a8c580-8aad-11e9-8281-567fe7f588f6.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![7_gray](https://user-images.githubusercontent.com/23094225/59155731-c1fbf100-8aad-11e9-8595-2fe7b2cadbae.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![7_predicted](https://user-images.githubusercontent.com/23094225/59155734-ce804980-8aad-11e9-8dd1-2a921eebb0a6.jpg)

![8](https://user-images.githubusercontent.com/23094225/59155738-e8ba2780-8aad-11e9-9ed3-bb3126d13668.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![8_gray](https://user-images.githubusercontent.com/23094225/59155739-f1aaf900-8aad-11e9-9b9a-6f82f26a9ded.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![8_predicted](https://user-images.githubusercontent.com/23094225/59155746-fbccf780-8aad-11e9-8ae9-734b894c21ae.jpg)


![9](https://user-images.githubusercontent.com/23094225/59155749-07b8b980-8aae-11e9-845c-b45d6585a66c.jpg)&nbsp;&nbsp;&nbsp;&nbsp;  ![9_gray](https://user-images.githubusercontent.com/23094225/59155755-14d5a880-8aae-11e9-834f-645b9f6ffa1a.jpg)  &nbsp;&nbsp;&nbsp;&nbsp;   ![9_predicted](https://user-images.githubusercontent.com/23094225/59155760-261eb500-8aae-11e9-9eaa-031900322edc.jpg)







