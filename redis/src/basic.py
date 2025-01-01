import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# Check specific keys
r.keys('*')

#------------
# Check number of keys in database
r.dbsize()

#------------
# set key value
r.set('key', 'value')
r.set('key', 'value', ex=10, nx=True)

#------------
# get value by key
value = r.get('key')
print(value)

#------------
# syntax : delete keys
r.delete('key')