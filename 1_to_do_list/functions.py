import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date


completed = []
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)

    def __repr__(self):
        return self.task


def add_row(string_to_check='', gui_string=''):
    todos = read_file()
    if string_to_check:
        todo = string_to_check[4:] + "\n"
    else:
        if gui_string:
            todo = gui_string + "\n"
        else:
            todo = input("Enter a todo: ") + "\n"
    todos.append(todo)
    write_file(todos)


def show_tasks():
    show_ennumerated_tasks(file_name='files/todos.txt')


def edit():
    print("Choose what to edit")
    todos = show_ennumerated_tasks()
    while True:
        edit_option = input("Type number or 'cancel'")
        if edit_option.isdigit() and int(edit_option) - 1 <= len(todos):
            new_value = input("What's new value? ") + "\n"
            old_value = todos[int(edit_option) - 1]
            todos[int(edit_option) - 1] = new_value
            write_file(todos)
            print(f"You replaced '{old_value.strip()}' with '{new_value.strip()}'")
            break
        elif edit_option.lower() == "cancel":
            break
        else:
            "Type number or 'exit'"


def complete():
    while True:
        print("Choose what to complete")
        todos = show_ennumerated_tasks()
        complete_option = input("Type number")
        if complete_option.isdigit() and int(complete_option) - 1 <= len(todos):
            completed = read_file('files/finished.txt')
            task_to_remove = todos[int(complete_option) - 1].strip()
            completed.append(todos.pop(int(complete_option) - 1))
            write_file(completed, 'files/finished.txt')
            write_file(todos)
            print(f"{task_to_remove} has been removed from the list")
            break
        else:
            print("Wrong number")


def show_finished_tasks():
    show_ennumerated_tasks(file_name='files/finished.txt')


def show_ennumerated_tasks(file_name='files/todos.txt', as_string=False):
    tasks = read_file(file_name)
    if tasks:
        for index, item in enumerate(tasks):
            print(f"{index + 1}) {item}")
        if as_string:
            return " ".join(tasks)
        return tasks
    else:
        print('The list is empty')
        if as_string:
            return ""
        return []



def print_rows(rows):
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for i in range(len(rows)):
            print(f'{str(i + 1)}. {str(rows[i])} {rows[i].deadline.strftime("%d %b")}')
    print('\n')



def show(tasks_list):
    for index, item in enumerate(tasks_list):
        print(f"{index + 1}) {item}")


def read_file(filename='files/todos.txt'):
    if not os.path.isfile(filename):
        file = open(filename, 'w')
        file.close()
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos


def write_file(text, filename='files/todos.txt'):
    with open(filename, 'w') as file:
        file.writelines(text)
