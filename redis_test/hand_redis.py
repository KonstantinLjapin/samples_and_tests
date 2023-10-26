import redis


class WorkerRedis:
    """
        Class: work with redis context manager
        init:  config(host, port)
        type work for redis
        with redis.Redis(host='localhost', port=6379, decode_responses=True) as r:
             r.hset('users_capcha_key_dict', mapping={'1234': '9999'}) add value map ~users
             r.hset('users_capcha_key_dict', mapping={'1234': '8888'}) change value map ~users
             r.hkeys('users_capcha_key_dict') get all keys value in map ~users
             r.hdel('users_capcha_key_dict', '1234') del value in map  ~users
             r.hgetall('users_capcha_key_dict')

             r.hset('users_captcha_flag_dict', mapping={'1234': 1}) add value map ~flag
             r.hset('users_captcha_flag_dict', mapping={'1234': 0}) change value map ~flag
             r.hget('users_captcha_flag_dict', '1234') get value map ~flag
             r.hkeys('users_captcha_flag_dict')

    """

    def __init__(self):
        self.__host: str = 'localhost'
        self.__port: int = 6379
        self.__users_map_name: str = 'users_capcha_key_map'
        self.__users_capcha_flag_map_name: str = 'users_capcha_flag_map'

    def _get_host(self) -> str:
        return self.__host

    def _get_port(self) -> int:
        return self.__port

    def _get_users_map_name(self) -> str:
        return self.__users_map_name

    def _get_capcha_flag_map_name(self) -> str:
        return self.__users_capcha_flag_map_name

    def add_capcha_key(self, user_id: int, capcha: int) -> None:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            r.hset(self._get_users_map_name(), mapping={str(user_id): capcha})

    def get_capcha_key(self, user_id: int) -> int:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            return int(r.hget(self._get_users_map_name(), str(user_id)))

    def get_all_capcha_user_key(self) -> list:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            return r.hkeys(self._get_users_map_name())

    def del_capcha_key(self, user_id: int) -> None:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            r.hdel(self._get_users_map_name(), str(user_id))

    def add_capcha_flag(self, user_id: int, flag: int) -> None:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            r.hset(self._get_capcha_flag_map_name(), mapping={str(user_id): flag})

    def get_capcha_flag(self, user_id: int) -> int:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            return int(r.hget(self._get_capcha_flag_map_name(), str(user_id)))

    def change_capcha_flag(self, user_id: int, flag: int) -> None:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            r.hset(self._get_capcha_flag_map_name(), mapping={str(user_id): flag})

    def del_capcha_flag(self, user_id: int) -> None:
        with redis.Redis(host=self._get_host(), port=self._get_port(), decode_responses=True) as r:
            r.hdel(self._get_capcha_flag_map_name(), str(user_id))


if __name__ == "__main__":
    redison = WorkerRedis()
    redison.add_capcha_key(1234, 1235)
    redison.add_capcha_flag(1234, 1)
    redison.add_capcha_key(1235, 1235)
    redison.add_capcha_flag(1235, 1)
    print(redison.get_capcha_key(1234), "capcha")
    print(redison.get_capcha_flag(1234), "flag")
    redison.change_capcha_flag(1234, 0)
    print(redison.get_capcha_flag(1234), "flag change")
    print(redison.get_all_capcha_user_key(), "all Keys")
    redison.del_capcha_key(1234)
    print(redison.get_all_capcha_user_key(), "all Keys")


