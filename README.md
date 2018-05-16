# Icon Hash
![image1](http://images.vfl.ru/ii/1526063901/490732a0/21705298.png)

We are making a DCGAN to generate newer variants of [Planets](https://drive.google.com/drive/folders/1NwupUPLIPuQZG38Lm1CT0vdofP6I5QgA?usp=sharing) (link to training dataset) from random noise inputs.

This Convolutional Generative Adversarial Networks mainly consists of two different networks, the genarator and the discriminator. The Generator tries to generates images from random noise and fools the discriminator in the process.

The Generator model consist of a block of layers that consist of Batchnormalization, upsampling followed by a convolution with relu activation. There are 4 such blocks used only the forth block contains tanh function as the activation of the convolution layer. The Discriminator model is a simple deep convolution network trying to distinguish between true or fake planet images. The combined model is compiled adam optimizer(learning rate=0.0002), with binary cross entropy loss. 
The training process for 7000 first iterations is shown in this gif below:
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
# iconhash.py script requires generator.json (generator network structure) 
# and gen.h5 (network weights) files, 
# they should be stored at the same folder as the main script.
cd Script

# To generate a 128x128 planet icon for address Parameter1 using DCGAN 
# and to store it in Parameter2 directiry run the following
.../python iconhash.py parameter1 parameter2
```
##### Parameter1 could be one of the following:
*  a Metahash Address (0x0083504341c15f066955c2ac999b356894cde5c20f5a0ee9ac)
* [file.tsv](https://github.com/metahashorg/iconhash_py/blob/master/example.tsv) a file containing several Metahash Addresses
* [file.txt](https://github.com/metahashorg/iconhash_py/blob/master/example.txt) a file containing several Metahash Addresses
##### Parameter2
* Output folder
##### Финальный результат
* Png файлы для каждого Matahash Adsress с изображением(иконкой) планеты (0x0083504341c15f066955c2ac999b356894cde5c20f5a0ee9ac.png) разрешением 128x128

## Пример использования скрипта
```
cd Script
/opt/anaconda3/bin/python iconhash.py example.txt ./Example/
```
Файл example.txt содержил 10 Matahash Adsress созданных при помощи скрипта [crypt_example.py](https://github.com/metahashorg/crypt_example_py)
В папке Example создалось 10 png файлов для каждого Matahash Adsress из файла example.txt
![image_test_all](http://images.vfl.ru/ii/1526465475/cb414f5b/21764534.png)

## Тест Matahash_Adsress_Mistake
Проверка скрипта на то, что при неправильном вводе одного или несколько символов в адресе, планета на иконке меняется кардинально. На вход скрипты подавались следующие Matahash Adsress:

0x002cfbe84acd405627302b35c081c36f8ebafb4df075ad9f70
0x002cfbe84acd405627302b35c081c36f8obafb4df075ad9f70
0x002cfbe84acd405627302b35c081c36f8odafb4df075ad9f70
0x002cfbe84acd405627302b35c0e1c36f8ebafb4df075ad9f70
0x002cfbe84acd405627302b35c0e7c36f8ebafb4df075ad9f70
0x002cfbe84acd405627302b35o081c36f8ebafb4df075ad9f70
0x002cfbe84acd405627302b85c081c36f8ebafb4df075ad9f70
0x002cfbe84acd4O5627302b35c081c36f8ebafb4df075ad9f70
0x002cfbe85acd405627302b35c081c14f8ebafb4df075ad9f70
0x002cfbe85acd405627302b35c081c36f8ebafb4df075ad9f70

Иконка планеты для каждого соответственно:
![image_test_mistake](http://images.vfl.ru/ii/1526466151/24da5a70/21764646.png)
