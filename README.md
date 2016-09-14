# auction_house

##依赖版本
* Python 2.7.12
* Django 1.10.1
* Mysql

##搭建方法
* 安装Python
* 安装Pip
* 安装Django
* 安装mysql-python驱动
* 根据 {path}/auction_house/auction_house/settings.py 中的DATABASES建立本地database
* 执行DB同步
    * python manage.py makemigrations
    * python manage.py migrate
* 运行server
    * cd {path}/auction_house
    * python manage.py runserver
* 访问主页
    * http://localhost:8000/

