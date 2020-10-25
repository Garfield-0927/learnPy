# paddleOcr

## 1.快速安装

1. **安装PaddlePaddle Fluid v2.0**

   ```
   pip3 install --upgrade pip
   
   如果您的机器安装的是CUDA9或CUDA10，请运行以下命令安装
   python3 -m pip install paddlepaddle-gpu==2.0.0b0 -i https://mirror.baidu.com/pypi/simple
   
   如果您的机器是CPU，请运行以下命令安装
   
   python3 -m pip install paddlepaddle==2.0.0b0 -i https://mirror.baidu.com/pypi/simple
   
   更多的版本需求，请参照[安装文档](https://www.paddlepaddle.org.cn/install/quick)中的说明进行操作。
   ```

   2.**克隆PaddleOCR repo代码**

   ```
   【推荐】git clone https://github.com/PaddlePaddle/PaddleOCR
   
   如果因为网络问题无法pull成功，也可选择使用码云上的托管：
   
   git clone https://gitee.com/paddlepaddle/PaddleOCR
   
   注：码云托管代码可能无法实时同步本github项目更新，存在3~5天延时，请优先使用推荐方式
   ```

   3.**安装第三方库**

   ```
   cd PaddleOCR
   pip3 install -r requirments.txt
   ```

   *4.**若git clone速度过慢，解决方法是修改hosts文件**

   ​		1.Hosts文件地址

   ```
   C:\Windows\System32\drivers\etc\hosts
   ```

   ​		2.IP地址查询

   ​		到[网站1](https://github.com.ipaddress.com/)或[网站2](https://www.ip138.com/)查询以下链接的IP地址

   ```
   github.com
   gist.github.com
   assets-cdn.github.com
   raw.githubusercontent.com
   gist.githubusercontent.com
   cloud.githubusercontent.com
   camo.githubusercontent.com
   avatars0.githubusercontent.com
   avatars1.githubusercontent.com
   avatars2.githubusercontent.com
   avatars3.githubusercontent.com
   avatars4.githubusercontent.com
   avatars5.githubusercontent.com
   avatars6.githubusercontent.com
   avatars7.githubusercontent.com
   avatars8.githubusercontent.com
   ```

   ​		3.将查询到的信息加入到hosts文件中，需要管理员权限，例如：

   ```
   # GitHub Start
   140.82.112.3 github.com
   140.82.114.4 gist.github.com
   185.199.108.153 assets-cdn.github.com
   199.232.68.133 raw.githubusercontent.com
   199.232.68.133 gist.githubusercontent.com
   199.232.68.133 cloud.githubusercontent.com
   199.232.68.133 camo.githubusercontent.com
   199.232.68.133 avatars0.githubusercontent.com
   199.232.68.133 avatars1.githubusercontent.com
   199.232.68.133 avatars2.githubusercontent.com
   199.232.68.133 avatars3.githubusercontent.com
   199.232.68.133 avatars4.githubusercontent.com
   199.232.68.133 avatars5.githubusercontent.com
   199.232.68.133 avatars6.githubusercontent.com
   199.232.68.133 avatars7.githubusercontent.com
   199.232.68.133 avatars8.githubusercontent.com
   # Github End
   ```

   ​		4.cmd刷新DNS缓存

   ```
   ipconfig /flushdns
   ```

## 2.中文OCR模型快速使用

​	**1.inference模型下载**

<img src=".\img\inference.png" alt="img" style="zoom: 50%;" />

​		以超轻量级模型为例：

```
mkdir inference && cd inference
# 下载超轻量级中文OCR模型的检测模型并解压
wget https://paddleocr.bj.bcebos.com/20-09-22/mobile/det/ch_ppocr_mobile_v1.1_det_infer.tar && tar xf ch_ppocr_mobile_v1.1_det_infer.tar
# 下载超轻量级中文OCR模型的识别模型并解压
wget https://paddleocr.bj.bcebos.com/20-09-22/mobile/rec/ch_ppocr_mobile_v1.1_rec_infer.tar && tar xf ch_ppocr_mobile_v1.1_rec_infer.tar
# 下载超轻量级中文OCR模型的文本方向分类器模型并解压
wget https://paddleocr.bj.bcebos.com/20-09-22/cls/ch_ppocr_mobile_v1.1_cls_infer.tar && tar xf ch_ppocr_mobile_v1.1_cls_infer.tar
cd ..
```

​		若没有安装wget，则[点击进入网站](https://github.com/PaddlePaddle/PaddleOCR/blob/develop/doc/doc_ch/quickstart.md)，直接进行下载，并解压放置在相应目录下

复制上表中的检测和识别的`inference模型`下载地址，并解压。

​		解压完毕后应有如下文件结构：

```
|-inference
    |-ch_ppocr_mobile_v1.1_det_infer
        |- model
        |- params
    |-ch_ppocr_mobile_v1.1_rec_infer
        |- model
        |- params
    |-ch_ppocr_mobile-v1.1_cls_infer
        |- model
        |- params
    ...
```

​	**2.单张图像或者图像集合预测**

​		以下代码实现了文本检测、识别串联推理，在执行预测时，需要通过参数image_dir指定单张图像或者图像集合的路径、参数`det_model_dir`指定检测inference模型的路径、参数`rec_model_dir`指定识别inference模型的路径、参数`use_angle_cls`指定是否使用方向分类器、参数`cls_model_dir`指定方向分类器inference模型的路径、参数`use_space_char`指定是否预测空格字符。可视化识别结果默认保存到`./inference_results`文件夹里面。

```
# 预测image_dir指定的单张图像
python tools/infer/predict_system.py --image_dir=./doc/imgs/11.jpg --det_model_dir=./inference/ch_ppocr_mobile_v1.1_det_infer/  --rec_model_dir=./inference/ch_ppocr_mobile_v1.1_rec_infer/ --cls_model_dir=./inference/ch_ppocr_mobile_v1.1_cls_infer/ --use_angle_cls=True --use_space_char=True

# 预测image_dir指定的图像集合
python tools/infer/predict_system.py --image_dir="./doc/imgs/" --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/"  --rec_model_dir="./inference/ch_ppocr_mobile_v1.1_rec_infer/" --cls_model_dir="./inference/ch_ppocr_mobile_v1.1_cls_infer/" --use_angle_cls=True --use_space_char=True

# 如果想使用CPU进行预测，需设置use_gpu参数为False
python tools/infer/predict_system.py --image_dir=./doc/imgs/11.jpg --det_model_dir=./inference/ch_ppocr_mobile_v1.1_det_infer/  --rec_model_dir=./inference/ch_ppocr_mobile_v1.1_rec_infer/ --cls_model_dir=./inference/ch_ppocr_mobile_v1.1_cls_infer/ --use_angle_cls=True --use_space_char=True --use_gpu=False
```

​		**踩坑实录：**

​	    官方文档上面的代码是python3 tools/infer/predict_system.py，但是我的机子上在cmd输入上面的命令没有用，只有输入将python3改成python才有用。

​		举个简单例子，我写了一个main.py，里面就print('Hi,PyCharm')。

![bug1.1](.\img\bug1.1.png)

![bug1.2](.\img\bug1.2.png)

- 通用中文OCR模型

请按照上述步骤下载相应的模型，并且更新相关的参数，示例如下：

```
# 预测image_dir指定的单张图像
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/11.jpg" --det_model_dir="./inference/ch_ppocr_server_v1.1_det_infer/"  --rec_model_dir="./inference/ch_ppocr_server_v1.1_rec_infer/" --cls_model_dir="./inference/ch_ppocr_mobile_v1.1_cls_infer/" --use_angle_cls=True --use_space_char=True
```

- 注意：
  - 如果希望使用不支持空格的识别模型，在预测的时候需要注意：请将代码更新到最新版本，并添加参数 `--use_space_char=False`。
  - 如果不希望使用方向分类器，在预测的时候需要注意：请将代码更新到最新版本，并添加参数 `--use_angle_cls=False`。

## 3.运行成果(用CUP进行预测)

![bug1.1](.\inference_results\11.jpg)



## 4. GPU预测环境配置

​			**参考教程：https://blog.csdn.net/weixin_45494025/article/details/100746025**

- 需要确认您的 Windows 7/8/10 是 64 位操作系统*
- 需要您具有*支持 CUDA 的 nVidia 显卡*，且正确安装 [CUDA 10](https://docs.nvidia.com/cuda/archive/10.0/index.html)
  注意：Windows 仅支持 CUDA 9.0/10.0 的单卡模式；不支持 CUDA 9.1/9.2/10.1
- 需要使用 [cuDNN 7.6+](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/#install-windows)
- Windows 暂不支持 NCCL
- 确认您需要安装PaddlePaddle 的 python版本是3.5.1+/3.6+/3.7+，*因为您计算机可能有多个python*

```
python --version
```

- 如果python版本不是3.5.1+/3.6+/3.7+，请您确认python的路径是否是您预期的位置

```
where python
```

- 其中python 3.5.1+/3.6+/3.7+的安装目录应位于第一行，如果不是，您可以通过以下任意方法调整：
  - 将所有命令行中的 `python`替换为 `python3`的安装路径（例如C:\Python36\python.exe)
  - 在环境变量中，将 `python3`的安装路径设置在第一顺序位（请在控制面板->系统属性->环境变量->PATH中修改)
- 如果python版本是3.5.1+/3.6+/3.7+，请确认 Python 有对应的 pip，检查 Python 对应的 pip 的版本，确认是 9.0.1+：

```
python -m ensurepip
python -m pip --version
```

- 确认 Python 和 pip 是 64 bit，并且处理器架构是x86_64（或称作 x64、Intel 64、AMD64）架构，目前PaddlePaddle不支持arm64架构
  下面的第一行输出的是 "64bit"，第二行输出的是 "x86_64"、"x64" 或 "AMD64" 即可：

```
python -c "import platform;print(platform.architecture()[0]);print(platform.machine())"
```

- 执行以下命令安装（推荐使用百度源）：

```
python -m pip install paddlepaddle-gpu==1.8.5.post107 -i https://mirror.baidu.com/pypi/simple
```

或

```
python -m pip install paddlepaddle-gpu==1.8.5.post107 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

验证信息

使用 `python` 进入python解释器，输入`import paddle.fluid` ，再输入 `paddle.fluid.install_check.run_check()`。
如果出现 `Your Paddle Fluid is installed successfully!`，说明您已成功安装。

说明信息

更多帮助信息请参考 [Windows 下 pip 安装](https://www.paddlepaddle.org.cn/documentation/docs/zh/1.8/install/install_Windows.html#windows)。
*同时要求处理器支持 MKL；并且架构是x86_64，PaddlePaddle不支持arm64架构

