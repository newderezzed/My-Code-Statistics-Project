import redis


# 创建连接
# conn = redis.Redis(host='47.94.172.250',port=6379,password='luffy1234')
# conn.set('x1','wanghuaqiang',ex=5)
# val = conn.get('x1')
# print(val)

# 连接池

# import redis
#
# pool = redis.ConnectionPool(host='10.211.55.4', port=6379,password='luffy1234',max_connections=1000)
# conn = redis.Redis(connection_pool=pool)
#
# conn.set('foo', 'Bar')


# 问题来了
from redis_pool import POOL


while True:
    key = input('请输入key:')
    value = input('请输入value:')
    # 创建连接池

    # 去连接池中获取连接
    conn = redis.Redis(connection_pool=POOL)
    # 设置值
    conn.set(key, value)





