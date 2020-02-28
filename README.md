# FudanPT-master-new
复旦大学研究生入学考试初试成绩爬取，都怪复旦大学不提供排名
>
>感谢学长提供的**FudanPT**开源项目https://github.com/CDOTAD/FudanPT

[![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) ![](https://img.shields.io/badge/django-2.0-green.svg) ![](https://img.shields.io/badge/BeautifulSoup-4.6.0-green.svg)

## Toy Level Website

为了快速上线函数名，文件名都是随便取的，以及没有做任何的安全措施，总之是个玩具级的网站。

网站只入库了专业代码为**085400**且公共课为**961**的软件专硕和**083500**的软件学硕。

## UPDATES:

修改数据库为sqlite3，无需nginx即可轻量上线，可刷新验证码

## GUIDE：

安装所需库：

django、bs4、sqlite、numpy

进入目录文件夹，准备迁移：

`python manage.py makemigrations`

`python manage.py migrate`
运行程序前请先创建sqlite3数据库
`python createdb.py`
后台运行django项目：

`nohup python manage.py runserver 0.0.0.0:8888 &`

Ok，输入浏览器打开“主机ip+:8888”即可访问！



