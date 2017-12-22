#Use youtube-dl下载YouTube视频[python skill]

##0 前言
会用梯子的小伙伴很多喜欢看YouTube视频，但是，想下载YouTube视频怎么办呢？有VPS的同学们
我们可以通过youtube-dl这个工具。youtube-dl是一个python编写的脚本，可以下载youtube等热
门视频网站的视频，使用起来也很简单。

这里需要关注下这三个网站：
>Youtube-dl Github项目地址：https://github.com/rg3/youtube-dl
>Youtube-dl 支持的视音频网站列表：http://rg3.github.io/youtube-dl/supportedsites.html
>FFmpeg 官网：http://www.ffmpeg.org/

本文主要分为四个部分：
<1>基础环境配置
<2>安装 Youtube-dl
<3>安装 FFmpeg
<4>下载 youtube 视频
这里以Linux为栗


##基础环境配置
不管是什么操作系统，在你安装软件之前，update 是绝对需要的，同时，我们在安装 Youtube-dl 的时候需要用到 wget，如果你的操作系统没有安装 wget ，需要先安装。也要用到 gcc，所以也要安装。
这里以Centos 7 为栗
```
yum update

yum install wget

yum install gcc

yum install gcc-c++

yum install make
```
若是Ubuntu,Maybe you can:
```
apt-get update

apt-get install wget

apt-get install build-essential

apt-get install make
```


##2 Install youtube-dl
youtube-dl直接下载最新版到/usr/local/bin/目录下并赋予权限即可使用。命令：

```
1.wget http://youtube-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
2.chmod a+x /usr/local/bin/youtube-dl
```
###youtube-dl用法
查看使用帮助
```
1.youyube-dl -h
```
介绍一些常用参数
```
1.youtube-dl --list-extractors  #查看支持网站列表
2.youtube-dl -U  #程序升级
3.youtube-dl --get-format URL #获取视频格式
4.youtube-dl -F URL #获取所有格式（目前仅支持YouTube），例如：
5.youtube-dl -F https://www.youtube.com/watch?v=nCfrfCzaB2A
6.--max-quality #下载的是上面的(best) 1280*720
#如果你想下真正的最高画质需要分别下上面的138和140，然后用视频软件合成。
#下载普通的视频只需要youtube-dl https://www.youtube.com/watch?v=nCfrfCzaB2A 默认下载下来的格式为webm
7.youtube-dl -f format URL #下载指定格式的视频，这里以下载1080p原画质量的视频格式为例:
8.youtube-dl -f 137 http://www.youtube.com/watch?v=n-BXNXvTvV4
```
注意一点：1080以上的视频音视频是分离的，需要装一下FFmpeg，debian下安装详见https://www.cmsky.com/debian-install-ffmpeg/ 然后-f 后面的数字之间选视频和音频部分用加号连着，例如youtube-dl -f 137+140，视频一定要在音频前面,FFmpeg会自动合并。

##3 Install FFmpeg
如果你不打算下载1080P 及以上分辨率的话，是没必要安装FFmpeg的。
安装 FFmpeg 的方法也很多，但是不区分操作系统的安装方法只有编译安装这个了，所以，就用这个方法吧。但是，FFmpeg 为了提高编译速度，使用了汇编指令，如果系统中没有 yasm 指令的话，得先装上。
需要注意的是，编译安装的时间会比较长，短的十几分钟，长的几个小时。建议使用screen（http://www.138vps.com/vpsjc/933.html）。
同时，编译很占 CPU，建议别选择对 CPU 限制比较大的商家

###1、Install yasm
```
wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz

tar -zxvf yasm-1.3.0.tar.gz

cd yasm-1.3.0

./configure

make

make install
```
如果出现：【make: *** No targets specified and no makefile found.  Stop.】请看注1


###2、Install FFmpeg
```
cd /root

wget http://www.ffmpeg.org/releases/ffmpeg-3.3.3.tar.gz

tar -zxvf ffmpeg-3.3.3.tar.gz

cd ffmpeg-3.3.3

./configure

make

make install

```
经过漫长的等级，终于编译完成了，我们可以查看所安装的ffmpeg版本
>ffmpeg -version
##4 Download YouTube 视频
下载 youtube 的视频就很简单了，比如下面这条命令，会自动下载最高分辨率的视频
>youtube-dl https://www.youtube.com/watch?v=SLaYPmhse30

![分辨率](http://www.138vps.com/content/uploadfile/201709/dd0b1504928314.jpg)
结果如图，请注意 format-code：
>audio only就是仅音频
>video only就是仅视频

如果你只是想下载720P的视频，那么通过观察上图，下载的时候把 format-code 加上即可：
>youtube-dl -f 22 https://www.youtube.com/watch?v=SLaYPmhse30

如果你想下载 1080P 的，那么除了下载视频外，还要把音频也下载下来，因为 youtube-dl 会自动调用 ffmpeg 合并音视频，所以我们只需下载就可以了，下载完成后，youtube-dl 会自动调用 ffmpeg 把音视频合并。
>youtube-dl -f 137+140 https://www.youtube.com/watch?v=SLaYPmhse30

##Remarks
注1:如果编译安装时出现问题，可能是某些依赖没装上。The solution is as follows:
**Centos**
```
yum install gcc gcc-c++ autoconf automake

yun -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel
```

**Ubuntu**
```
apt-get install gcc build-essential
```
next 从【 ./configure 】命令从新开始

注2：若为windows 可参考http://www.jianshu.com/p/8817a7b0c8d6