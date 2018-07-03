from flask import Blueprint, render_template, Flask, request, redirect, session ,redirect
import os
import uuid
from ..utils import helper

ind = Blueprint('ind', __name__)


@ind.before_request
def process_request():
    """
    session自定义中间件
    :return:
    """
    if not session.get('user_info'):
        return redirect('/login')

    return None


@ind.route('/index')
def index():
    '''
    登陆后跳转主站
    :return:
    '''
    return redirect('/user_list')


@ind.route('/user_list',methods=['GET', 'POST'])
def user_list():
    """
    所有用户列表
    :return:
    """
    data_list = helper.fetch_all('select code_record.count,user.id,user.username,user.nickname from USER,CODE_RECORD WHERE USER.id=CODE_RECORD.user', [])
    if request.method == 'POST':
        page_sql_list = helper.fetch_all('select sum(code_record.count) AS count,user.username from USER,CODE_RECORD WHERE user.id=code_record.user group by user.username',[])
        print(page_sql_list)
        for i in page_sql_list:
            i['count'] = float(i['count'])
        print(page_sql_list)
        import json
        json_data_list = json.dumps(page_sql_list)
        return json_data_list

    return render_template('index.html', data_list=data_list)


@ind.route('/detail/<int:nid>',methods=['GET', 'POST'])
def detail(nid):
    '''
    用户个人提交记录
    :param nid:
    :return:
    '''
    import datetime
    record_list = helper.fetch_all('select id,count,date from CODE_RECORD WHERE user=%s', (nid,))
    print(record_list)
    if request.method == "POST":
        for i in record_list:
            if isinstance(i['date'],datetime.datetime):
                i['date'] = i['date'].strftime("%Y-%m-%d")
        import json
        json_data_list = json.dumps(record_list)
        print(json_data_list)
        return json_data_list

    return render_template('detail.html', record_list=record_list)


@ind.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    file_obj = request.files.get('code')

    # 1. 检查上传文件后缀名
    name_ext = file_obj.filename.rsplit('.', maxsplit=1)
    if len(name_ext) != 2:
        return "请上传zip压缩文件"
    if name_ext[1] != 'zip':
        return "请上传zip压缩文件"

    # 2+3, 接收用户上传文件，并解压到指定目录
    import shutil
    target_path = os.path.join('files', str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj.stream, target_path)

    # 4. 遍历某目录下的所有文件

    total_num = 0
    for base_path, folder_list, file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num

    # 获取当前时间
    import datetime
    ctime = datetime.date.today()
    print(total_num, ctime, session['user_info']['id'])

    data = helper.fetch_one("select id from CODE_RECORD where date=%s and user=%s", (ctime, session['user_info']['id']))
    if data:
        return "今天已经上传过了 请明天再试哦"

    helper.insert("insert into CODE_RECORD(count,date,user)values(%s,%s,%s)",
                  (total_num, ctime, session['user_info']['id']))

    return 'upload success, thank you '
