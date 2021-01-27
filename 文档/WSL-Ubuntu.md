# Ubuntu环境配置

## 创建root密码

```bash
sudo passwd root
```

## 更换自动镜像源

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.copy
```

```vim
sudo vim /etc/apt/sources.list
deb mirror://mirrors.ubuntu.com/mirrors.txt focal main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt focal-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt focal-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt focal-security main restricted universe multiverse
# 预发布软件源，不建议启用
# deb mirror://mirrors.ubuntu.com/mirrors.txt focal-proposed main restricted universe multiverse
```

## MySQL相关

```bash
# 安装
apt install mysql-server
# 修改配置文件
vim /etc/mysql/mysql.conf.d/mysqld.cnf
# 允许远程连接
bind-address =0.0.0.0
# 如果启用了ufw
ufw allow 3306
# 启动mysql服务
service mysql start
```

```MySQL
use mysql;
# 查看当前一些用户的账号和密码
select host,user,plugin,authentication_string from user;
ALTER USER 'root'@'localhost' IDENTIFIED WITH CACHING_SHA2_PASSWORD BY 'Clz19960522.';
# 刷新，使修改生效
flush privileges;
# 继续登录到mysql控制台进行操作，设置允许所有用户都可以通过root账号来访问
update user set host = '%' where user = 'root';
flush privileges;
```

## Python相关 (<https://www.python.org/downloads/source/>)

1. Python3-venv

```bash
py -m venv blog_venv
source blog_venv/bin/activate
```

```bash
# 完全卸载python3（软件及相关配置）
sudo apt-get remove --purge python3
# 完全卸载python3及其依赖软件（慎用！这里会删除python3及依赖python3的软件包，一般上面第一条命令已经够用）
sudo apt-get remove --auto-remove python3
sudo apt-get purge --auto-remove python3
# 清除python3.4及其依赖软件的安装包
sudo apt-get autoclean python3

wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
tar -zxvf Python-3.9.1.tgz
# 删除Python后出现无法编译情况下载build-essential 提供C/C++的编译环境
sudo apt-get install build-essential
./configure --prefix=/usr/local
make&&sudo make install

# 建立python3.X软链接
which python3.9
ln -s /usr/local/bin/python3.9 /usr/local/bin/py
# 解除软链接
sudo unlink xxname
```
