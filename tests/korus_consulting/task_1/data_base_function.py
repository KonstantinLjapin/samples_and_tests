import sqlite3
import os


def task_1():
    db_name = './task_1/library.db'
    database = sqlite3.connect(db_name)
    cursor = database.cursor()
    cursor.execute("SELECT MAX(Количество_страниц) FROM book WHERE Дата_поступления_в_библиотеку = '01.02.2022'")
    for book in cursor.fetchall():
        print(f"максимальное количеством страниц {book[0]}")
    cursor.execute("SELECT * FROM book WHERE Название = 'Change deep material perhaps.'")
    for book in cursor.fetchall():
        print(f"Книга с названием: Change deep material perhaps {book}")


if __name__ == "__main__":
    pass
