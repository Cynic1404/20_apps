from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
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



def add_row(task='This is string field!', deadline=datetime.today()):
    session = connect_db()
    new_row = Table(task=task, deadline=deadline)
    session.add(new_row)
    session.commit()

def show_tasks():
    rows = connect_db().query(Table).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for i in range(len(rows)):
            print(str(i + 1)+'. '+ str(rows[i]))



def connect_db():
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session()


if __name__ == '__main__':
    while True:
        print('''1) Today's tasks
2) Add task
0) Exit''')
        option = input('\n')
        if option == '2':
            add_row(task=input('Enter task\n'))
            print('The task has been added!')
        elif option == '1':
            print('Today:')
            show_tasks()
        elif option == '0':
            engine = create_engine('sqlite:///todo.db?check_same_thread=False')
            Base.metadata.create_all(engine)
            session = sessionmaker(bind=engine)
            quit()
        else:
            print('wrong option, try again\n')