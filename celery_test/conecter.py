import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

r.set('foo', 'bar')

print(r.get('foo'))
