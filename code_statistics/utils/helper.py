import pymysql
from settings import Config

def connect():
    """
    开始连接
    :return:
    """
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn,cursor


def connect_close(conn,cursor):
    """
    关闭连接
    :param conn:
    :param cursor:
    :return:
    """
    cursor.close()
    conn.close()

def fetch_all(sql,args):
    """
    全部获取
    :param sql:
    :param args:
    :return:
    """
    conn,cursor = connect()

    cursor.execute(sql, args)
    record_list = cursor.fetchall()
    connect_close(conn,cursor)

    return record_list


def fetch_one(sql, args):
    """
    只拿一条
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = connect()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    connect_close(conn, cursor)

    return result


def insert(sql, args):
    """
    增加
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = connect()
    row = cursor.execute(sql, args)
    conn.commit()
    connect_close(conn, cursor)
    return row