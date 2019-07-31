# djangoStart
 django初始化项目结构
# 流程
. python3 -m venv djangoStart
. source djangoStart/bin/activate
. (pip install --upgrade pip)
. pip install django
. 转到项目目录下 django-admin startproject 项目名
. pip install mysqlclient
. pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
. pip install django-ckeditor Pillow

. 解决xadmin添加用户小组件bug
    render() got an unexpected keyword argument 'renderer
    \xadmin\views\dashboard.py

    第36行
    https://github.com/sshwsfc/xadmin/issues/623
    def render(self, name, value, attrs=None, renderer=None):  # 修改bug：添加renderer

. 注册  'crispy_forms', 'xadmin',
. 注册 'ckeditor', 'ckeditor_uploader',
. (ckeditor需要静态css )collectstatic
. startapp
. makemigrations migrate createsuperuser
. pip freeze > requirements.txt