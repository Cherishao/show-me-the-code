# ImportError: No module named gevent

导入错误：没有叫gevent的模块

## 0 前言

I am new to the Python application development in Ubuntu.

> 在Ubuntu下进行Python的应用程序开发，我是一个新手。

I would try to be concise but please forgive and ask me if my explanations is too unclear to understand. I would be appreciated for your answers.

> 我会尽量简明扼要，如果我的解释不太明确难以理解，请原谅，并问我。我很感激你的回答。

1- I have created a virtual environment for a project using “virtualenv” command called cyoa.

>在一个项目中我使用 “virtualenv”  的cyoa命令创造了一个虚拟的环境

2- PostGres DB is installed and I have created user name and password to connect to the database.

>安装了Postgres DB，我创建好了用户名和密码来连接数据库

3- The environment variable is like follow:

> 环境变量如下

```bash
#!/bin/bash

export DEBUG=False

export SECRET_KEY='supersecretproductionkeyforapp'

export DATABASE_URL='postgres://username:password@localhost/cyoa'

# Redis settings

export REDIS_SERVER='localhost'

export REDIS_PORT='6379'

export REDIS_DB='1'

# Twilio settings

export TWILIO_ACCOUNT_SID=''

export TWILIO_AUTH_TOKEN=''

export TWILIO_NUMBER=''

# Celery

export CELERY_BROKER_URL='redis://localhost:6379/0'

export CELERY_RESULT_BACKEND='redis://localhost:6379/0'
```

4- When I activate the virtual environment and try to run the following script

> 当我激活虚拟环境，试图运行下列脚本的时候

```bash
(cyoa)$ python manage.py syncdb
```

First lines of the manage script (which error is related to):

> 管理脚本的第一行，错误与此相关

```python
from gevent import monkey
monkey.patch_all()

import os
import redis
```

I get the following error:

> 我得到了下列错误

```Python
Traceback (most recent call last):
File "manage.py", line 1, in <module>
from gevent import monkey
ImportError: No module named gevent
```

gevent final version is installed using the command:

> 使用命名安装gevent最终版本

```bash
$sudo pip install gevent
```

