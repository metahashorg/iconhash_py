# Icon Hash
![image1](http://images.vfl.ru/ii/1526063901/490732a0/21705298.png)

We are making a DCGAN to generate newer variants of [Planets](https://drive.google.com/drive/folders/1NwupUPLIPuQZG38Lm1CT0vdofP6I5QgA?usp=sharing) (link to training dataset) from random noise inputs.

This Convolutional Generative Adversarial Networks mainly consists of two different networks, the genarator and the discriminator. The Generator tries to generates images from random noise and fools the discriminator in the process.

The Generator model consist of a block of layers that consist of Batchnormalization, upsampling followed by a convolution with relu activation. There are 4 such blocks used only the forth block contains tanh function as the activation of the convolution layer. The Discriminator model is a simple deep convolution network trying to distinguish between true or fake pokemon images. The combined model is compiled adam optimizer(learning rate=0.0002), with binary cross entropy loss. 
The training process for 7000 iterations is shown in this gif below:
<p align="center">
  <img width="250" height="250" src="https://github.com/metahashorg/iconhash_py/blob/master/output.gif">
</p>

## Dependencies
```
pip install
```
* Python 3
* Numpy
* Hashlib
* Pandas
* Scipy
* Keras 2.0.6+
* TensorFlow 1.2.1+

## Usage
```
# The folder should be three files (iconhash.py, generator.json, gen.h5)
cd Script

# Generate 128x128 planet icon using DCGAN
.../python iconhash.py [parameter1] [parameter2]
```
##### Parameter1
* Metahash Address (0x0077EA346BCE078C4701FB1C2B8031CBE9358D897A164879DF)
* [file.tsv](https://github.com/metahashorg/iconhash_py/blob/master/example.tsv) with Metahash Addresses
* [file.txt](https://github.com/metahashorg/iconhash_py/blob/master/example.txt) with Metahash Addresses
##### Parameter1
* Output folder

