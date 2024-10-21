# <div align="center">LiteGfm</div>
**<div align="center">A lightweight self-supervised monocular depth estimation model for artifacts reduction via guided image filtering</div>**

<div align="center"><font size='1'>Zhilin He, Yawei Zhang, Jingchang Mu, Xiaoyue Gu, and Tianhao Gu*</font>

![](https://img.shields.io/badge/license-MIT-blue) 
</div>

-----------
## Contents
* [Overview](#Overview)
* [Results](#Results)
    * KITTI
* [Data Preparation](#文本)
* [Single Image Test](#标题)
    * Preparing Trained Model
    * Start Testing
* [Evaluation](#文本)
* [Training](#文本)
    * Dependency Installation
    * Start Training
* [Citation](#文本)

-----------
### Overview
![overview]( /img/overview.png "The Overview of LiteGfm")

-----------
### Results
#### KITTI
<div align="center">
    
| model  | params|ImageNet Pretrained| Abs Rel|Sq Rel|RMSE|RMSE log|delta < 1.25|delta < 1.25^2|delta < 1.25^3|
|:-------------------:|:-----:|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| LiteGfm   | 1.9M | no |0.117 |0.871 |4.797 |0.194| 0.870| 0.957| 0.981|
| LiteGfm-small| 1.7M|no|0.123 |0.924| 4.922 |0.199| 0.858| 0.953 |0.980|
</div>
Click on the links in the 'model' column to download a trained model.

----------
### Data Preparation
Please refer to Monodepth2![](https://github.com/nianticlabs/monodepth2) to prepare your KITTI data.

----------
### Single Image Test
preparing trained model
From the table you can download trained models (depth encoder and depth decoder).

start testing 
```python
python test_simple.py --load_weights_folder path/to/your/weights/folder --image_path path/to/your/test/image
```
--------
### Evaluation
```python
python evaluate_depth.py --load_weights_folder path/to/your/weights/folder --data_path path/to/kitti_data/ --model liteGfm
```
---------
### Training
#### dependency installation
```python
pip install 'git+https://github.com/saadnaeem-dev/pytorch-linear-warmup-cosine-annealing-warm-restarts-weight-decay'
```
#### start training
```python
python train.py --data_path path/to/your/data --model_name mytrain --num_epochs 60 --batch_size 12 --lr 0.0005 5e-6 31 0.0001 1e-5 31
```
