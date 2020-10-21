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

   *4.**若git clone速度过慢**

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