from random import randint

from peewee import *
db = SqliteDatabase('people.db')


class ResponseModel(Model):
    chat_id_key = IntegerField()
    chat_id = IntegerField()
    key_request = TextField()
    city = TextField()
    date_in = TextField()
    date_out = TextField()
    photos = TextField()
    list_len = TextField()
    price_min = TextField()
    price_max = TextField()
    long_distance_too_centre = BlobField()

    class Meta:
        database = db
        table_name = 'response'


class ItemModel(Model):
    chat_id_key = IntegerField()
    intermediat = TextField()
    urls_photo = TextField()
    response = ForeignKeyField(ResponseModel, related_name='items')

    class Meta:
        database = db
        table_name = 'item'


def start():
    """create db and table"""
    try:
        db.connect()
        db.create_tables([ResponseModel, ItemModel])
    except Exception as error:
        print(error)
    db.close()


def data_base_con(user, list_hotel):
    """write in db"""
    key_gen = randint(1111, 9999)
    if user.price_long:
        pass
    else:
        temp = ['not', 'not', 'not']
        user.price_long = temp
    db.connect()
    resp = ResponseModel(chat_id_key=key_gen, chat_id=str(user.chat_id), key_request=str(user.key_request), city=str(user.city),
                         date_in=str(user.date_in), date_out=str(user.date_out), photos=str(user.photos),
                         list_len=str(user.list_len), price_min=str(user.price_long[0]),
                         price_max=str(user.price_long[1]),
                         long_distance_too_centre=str(user.price_long[2]), is_relative=True)
    resp.save()
    for obj in list_hotel:
        if user.photos.isdigit():
            ItemModel.create(chat_id_key=key_gen, response=resp, intermediat=obj[0][0], urls_photo=','.join(flatten(obj[1])))
        else:
            ItemModel.create(chat_id_key=key_gen, response=resp, intermediat=obj, urls_photo='-')
    db.close()


def check_user_in_db(chat_id) -> Tuple:
    """print history"""
    db.connect()
    query = ResponseModel.get(ResponseModel.chat_id == str(chat_id))
    photo_q = ItemModel.get(ItemModel.chat_id_key == query.chat_id_key)
    db.close()
    temp = f'{query.chat_id}' + f' {query.key_request} ' + f' {query.city}' \
           + '\n' + f' {query.date_in} ' + f' {query.date_out} ' + f'{query.photos}'
    return photo_q, temp


def flatten(s):
    """flat list"""
    if s == []:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])

if __name__ == '__main__':
    pass
