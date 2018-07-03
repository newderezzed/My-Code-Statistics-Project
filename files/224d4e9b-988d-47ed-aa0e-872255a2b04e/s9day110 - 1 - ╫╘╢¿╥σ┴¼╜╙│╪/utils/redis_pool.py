# by luffycity.com
import redis

POOL = redis.ConnectionPool(host='10.211.55.4', port=6379,password='luffy1234',max_connections=1000)
