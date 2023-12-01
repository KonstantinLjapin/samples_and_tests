from peewee import *

db = SqliteDatabase('people.db')


class UserModel(Model):
    chat_id = IntegerField()
    key_request = TextField()
    city = TextField()
    date_in = TextField()
    date_out = TextField()
    photos = TextField()
    list_len = IntegerField()
    price_min = IntegerField()
    price_max = IntegerField()
    long_distance_too_centre = BlobField()

    class Meta:
        database = db


def start():
    try:
        db.connect()
        db.create_tables([UserModel])
        db.close()
    except Exception as error:
        print(error)


def data_base_con(user):
    """write in db"""
    db.connect()
    some = UserModel.create(first_name=user.first_name, last_name=user.last_name, key_id=user.id)
    some.save()
    db.close()


def check_user_in_db(user):
    for user_select in UserModel.select():
        if user_select.chat_id == user.chat_id:
            print(user_select)
            db.close()
    print('all')


if __name__ == '__main__':
    pass
