from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)

    def __repr__(self):
        return self.task



def add_row(task='This is string field!', deadline=datetime.today().date()):
    session = connect_db()
    new_row = Table(task=task, deadline=deadline)
    session.add(new_row)
    session.commit()



def show_tasks(date=None):
    if date:
        rows = connect_db().query(Table).filter(Table.deadline == datetime.strptime(date, '%Y-%m-%d').date()).all()
    else:
        rows = connect_db().query(Table).order_by(Table.deadline).all()
    print_rows(rows)
    return rows

def show_missed_tasks():
    rows = connect_db().query(Table).filter(Table.deadline < datetime.date(datetime.today())).order_by(Table.deadline).all()
    print_rows(rows)


def weeks_tasks():
    for i in range(7):
        print((datetime.today() + timedelta(days=i)).strftime('%A %d %b'))
        show_tasks(date=(datetime.today()+timedelta(days=i)).strftime('%Y-%m-%d'))


def delete_task():
    delete_session = connect_db()
    rows = delete_session.query(Table).order_by(Table.deadline).all()
    if len(rows) == 0:
        print('Nothing to delete \n')
    else:
        print('Chose the number of the task you want to delete:')
        print_rows(rows)
        row_to_delete = rows[int(input(''))-1]
        delete_session.delete(row_to_delete)
        delete_session.commit()

def print_rows(rows):
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for i in range(len(rows)):
            print(f'{str(i + 1)}. {str(rows[i])} {rows[i].deadline.strftime("%d %b")}')
    print('\n')

def connect_db():
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session()


if __name__ == '__main__':
    while True:
        print('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')
        option = input('\n')
        if option == '1':
            print(f'Today {datetime.today().strftime("%d %b")}')
            show_tasks(datetime.now().strftime('%Y-%m-%d'))
        elif option == '2':
            weeks_tasks()
        elif option == '3':
            show_tasks()
        elif option == '4':
            show_missed_tasks()
        elif option == '5':
            add_row(task=input('Enter task\n'), deadline=datetime.strptime(input('Enter deadline. Format YYYY-MM-DD\n'),'%Y-%m-%d').date())
            print('The task has been added!')
        elif option == '6':
            delete_task()
        elif option == '0':
            quit()
        else:
            print('wrong option, try again\n')

