import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# set key value
r.lpush('key', *[1, 2, 3])

val = r.rpop('key')
print(val)