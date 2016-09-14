# auction_house

1.依赖版本
Python 2.7.12
Django 1.10.1
Mysql

2.搭建方法
（1）安装Python
（2）安装Pip
（3）安装Django
（4）安装mysql-python驱动
 (5) 根据 {path}/auction_house/auction_house/settings.py 中的DATABASES建立本地database
 (6)执行DB同步
	python manage.py makemigrations
	python manage.py migrate
 (7)运行server
 	cd {path}/auction_house
 	python manage.py runserver
 (8)访问主页
 	http://localhost:8000/
