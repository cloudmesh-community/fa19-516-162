## MNIST Deep Learning Example

The MNIST database contains around 60,000 images of handwritten digits. This 
database is used as a standard for training various image processing deep 
learning systems. As a part of this project, a simple neural network with two 
dense layers and one activation layer was created. This code is saved on the 
Oracle cloud object storage. We download the file using the Oracle storage put 
command.

```bash
$ cms storage --storage=oracle get ‘big-data\mnist-deep-learning.py’ 
‘mnist-deep-learning.py’
```

The downloaded file is then executed.

python 'mnist-deep-learning.py'

```bash
$ exec(open(‘mnist-deep-learning.py’.read())
```

![Model Benchmark](images/model-benchmark.png)

![Model Loss](images/model-loss.png)

![Model Accuracy](images/model-accuracy.png)
