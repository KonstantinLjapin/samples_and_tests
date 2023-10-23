import os
import csv
from pathlib import Path


def catch_csv(task_number):
    """this function finds the file path by number, return path"""
    dirs_list = []
    csv_list = []
    dir_path = Path.cwd()
    cur_pack = "csv_to_task"
    cur_dir = Path(dir_path, cur_pack)
    for root, dirs, files in os.walk(cur_dir):
        for d in dirs:
            dirs_list.append(d)
    for dir_name in dirs_list:
        if task_number in dir_name:
            for root, dirs, files in os.walk(Path(cur_dir, dir_name)):
                for filename in files:
                    csv_list.append(Path(cur_dir, dir_name, filename))
    return csv_list


def r_data(temp_path):
    """this function open in context, return list"""
    with open(catch_csv(temp_path)[1]) as f:
        reader = csv.reader(f)
        cur_list = []
        for row in reader:
            cur_list.append(''.join(row))
        return cur_list


if __name__ == "__main__":
    pass
