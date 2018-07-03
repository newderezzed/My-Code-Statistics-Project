from flask import Blueprint, render_template, Flask, request, redirect, session
from ..utils.md5 import md5
from ..utils import helper

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    pwd_md5 = md5(password)

    print(username)
    print(pwd_md5)

    data = helper.fetch_one('select id,nickname from USER WHERE username=%s and password=%s', (username, pwd_md5))
    print(data)

    if not data:
        return render_template('login.html', error='用户名密码错误')

    # 给session里设置值
    session['user_info'] = {
        'id': data['id'],
        'nickname': data['nickname'],
    }

    return redirect('/index')


@account.route('/logout', methods=['GET',])
def logout():
    session.pop('user_info')

    return redirect('/login')