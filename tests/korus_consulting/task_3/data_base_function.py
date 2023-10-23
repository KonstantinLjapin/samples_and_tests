import sqlite3
import os


def departments():
    db_name = './task_3/ledger.db'
    database = sqlite3.connect(db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM departments")
    temp = []
    for b in cursor.fetchall():
        temp.append(b)
    return temp


def transactions():
    db_name = './task_3/ledger.db'
    database = sqlite3.connect(db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM operations")
    temp = []
    for b in cursor.fetchall():
        temp.append(b)
    return temp


def calculator(*args):
    dep = args[0]
    trans = args[1]
    out_list = []
    temp_list_mounts = []
    for department in dep:
        dep_id, start_year, end_year, name = department
        for transact in trans:
            tr_id, year, month, day, department_id, income = transact
            if int(day) == 0 or int(day) > 31 or int(month) > 13 or int(year) < int(start_year):
                pass
            elif dep_id is department_id:
                if temp_list_mounts and int(month) > int(temp_list_mounts[1]):
                    out_list.append(temp_list_mounts)
                    temp_list_mounts = []
                if temp_list_mounts:
                    temp_list_mounts = [year, month, name, int(temp_list_mounts[3]) + int(income)]
                else:
                    temp_list_mounts = [year, month, name, int(income)]
    for i in out_list:
        print(i)


if __name__ == "__main__":
    pass
