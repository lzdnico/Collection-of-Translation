# 脚本功能
[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
  - 项目基于Flask框架
  - 项目基于selenium 爬虫
  ![image](https://github.com/lzdnico/Collection-of-Translation/blob/master/images/1.png) 
  ![image](https://github.com/lzdnico/Collection-of-Translation/blob/master/images/2.png) 
# 环境搭建及运行
  - 1.安装python3 依赖： 
  ```bash
  apt install -y python3-pip  git python3
  ```
  - 2.下载源码：
  ```bash
  cd 
  git clone https://github.com/lzdnico/Collection-of-Translation.git
  ```
  - 3.安装库： 
  ```bash
  cd Collection-of-Translation
  pip3 install -I -r requirements.txt 
  ```
  - 4.安装PhantomJS：
  ```bash
  wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
  tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 
  cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/ 
  ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
  ```

  - 5.后台运行：
  ```bash
  python3 api.py
  ```
```
# 联系我
  - 更新频道：https://t.me/niconewbeeeapi
  - 打赏地址:https://t.me/niconewbeeeapi/134
