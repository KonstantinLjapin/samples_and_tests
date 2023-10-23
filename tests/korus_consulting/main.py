from task_1 import task_1
from task_2 import positive_row
from task_3 import calculator, departments, transactions
import os

if __name__ == "__main__":
    print("task_1")
    task_1()
    print("task_2")
    positive_row("2")
    print("task_3")
    calculator(departments(), transactions())


