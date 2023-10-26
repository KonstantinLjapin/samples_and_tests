import redis

"""
with redis.Redis(host='localhost', port=6379, decode_responses=True) as r:
    r.hset('users_capcha_key_dict', mapping={'1234': 'Bill'})
    r.hset('users_captcha_flag_dict', mapping={'1234': 1})
    print(r.hget('users_captcha_flag_dict', '1234'))
    r.hset('users_captcha_flag_dict', mapping={'1234': 0})
    print(r.hget('users_captcha_flag_dict', '1234'))
    r.hset('users_capcha_key_dict', mapping={'6237': 'Hoi'})
    print(r.hkeys('users_capcha_key_dict'))
    print(r.hkeys('users_captcha_flag_dict'))
    #redis.hdel('users_capcha_key_dict', ['1234'])
    print(r.hgetall('users_capcha_key_dict'))
    r.hdel('users_capcha_key_dict', '1234')
    print(r.hgetall('users_capcha_key_dict'))
"""

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.hset('users_capcha_key_dict', mapping={'1234': 'Bill'})
print(r.hkeys('users_capcha_key_dict'))
