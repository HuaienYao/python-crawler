# 背景
最近对python爬虫感兴趣，参考了网上的教程，试着做一下。

这个就随时更新吧

# 笔记
## 使用git管理
### git的同步几个常用命令
```
# 在要同步的文件夹下初始化git
git init

# 关联到github远程仓库
git remote add origin git@github.com:HuaienYao/python-crawler.git

# 在文件改动后将修改状况提交到暂存区
git add .

# 添加改动说明，例如'增加了readme'
git commit -m "增加了readme"

# 推送暂存区的文件到github远程仓库
git push -u origin master
```
以上只是为了忘记的时候可以拿来看看。

如果在新的设备上要克隆下远程仓库文件，就用下列的命令
```
git clone git@github.com:HuaienYao/python-crawler.git
```
这里附上git pull和git clone的区别
> 一、git pull命令用于取回远程主机某个分支的更新与本地的指定分支合并。
> 二、git clone是把整个git项目拷贝下来，包括里面的日志信息，git项目里的分支，你也可以直接切换、使用里面的分支等等

来源:https://blog.csdn.net/kucoffee12/article/details/75252858

## 初识python爬虫
### 原理
python爬虫的原理就是将一个网页的源码打印出来并分析，使用正则表达式来匹配相关条件来获取需要的信息。

比如把html网页的源码分析后，根据各个html标签来定位该信息。

### pycharm的配置
#### 安装库
pycharm在安装后就可以使用，但是如果没有额外安装需要的库的话，导入的库无作用。比如我们需要用到beautiful soup这个爬虫框架，但是pycharm安装后里面并没有，需要自己手动安装。

```
菜单栏上的 File > Settings > Project > Project Interpreter 里面搜索到你需要的库来点击下方的Install 来安装。
```



# 教程列表
- https://morvanzhou.github.io/
