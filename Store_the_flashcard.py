# 2/4
"""In the previous stage, we created our first flashcards. The downside is that they are lost every time you close the program. We need to find a way to store them. We can use an SQLite database for this purpose. This database consists of a single file and is easy to install. To process this type of database with Python rather than SQL, we need Object Relational Mapper (ORM). SQLAlchemy can translate the Python classes to tables in relational databases and convert the function calls to SQL statements automatically.
When establishing a connection with the database, you should add a check_same_thread=False flag to the database name so that Hyperskill can test your project properly
engine = create_engine('sqlite:///<your database name.db>?check_same_thread=False')

After that, we need to create tables in the database so that the declarative_base() function can establish a base class. A base class stores a catalog of classes and mapped tables in the declarative system.

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Once the base class is declared, we can define any number of mapped classes inside. For now, we want to store the answers and questions in the database. To do that we need to define the following class:
from sqlalchemy import Column, Integer, String

class MyClass(Base):
    __tablename__ = 'my_table'

    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)
A class in declarative must have a __tablename__ attribute and at least one Column that constitutes a primary key.

We also need to call the MetaData.create_all() method to create the corresponding table in the database.
Base.metadata.create_all(engine)
Now, you should create a session. And, finally, you are ready to add a new object to the table:

new_data = MyClass(first_column='What is the capital city of India', second_column='New Delhi')
session.add(new_data)
session.commit()
The added data will be pending until we call the commit() method.

The query(<mapped class name>) method can help you access the table data.

result_list = session.query(MyClass).all()
This code snippet above includes the all() method that returns a list of all added objects.

print(result_list[0].question)  # What is the capital city of India
print(result_list[0].answer)    # New Delhi
print(result_list[0].id)        # 1

Objectives
In this stage, your program should implement the features from Stage 1 and do the following:

Create a database. Please, name it flashcard: this will ensure the proper work of the tests (even though the tests will not check the file with the database itself).
Create a table in the database, name it flashcard.
Store a question in each table row with an answer and an ID.
"""
from create_db import engine, Base, Flashcard
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def check_input(input_value, list_check):
    try:
        if int(input_value) in list_check:
            return int(input_value)
        else:
            print(f"{input_value} is not an option")
            print()
            return f"{input_value} is not an option"
    except ValueError:
        print(f"{input_value} is not an option")
        print()
        return f"{input_value} is not an option"


def print_main_menu():
    print('1. Add flashcards')
    print('2. Practice flashcards')
    print('3. Exit')


def print_add_menu():
    print()
    print('1. Add a new flashcard')
    print('2. Exit')


def loop_for_input(choice, list_choice, function):
    while choice not in list_choice:
        if function == 'main':
            print_main_menu()
        if function == 'add':
            print_add_menu()
        choice = input()
        choice = check_input(input_value=choice, list_check=list_choice)
    return choice


def main():
    dictionary_flashcard = {}
    list_choice_1 = [1, 2, 3]
    choice_1 = 0
    while choice_1 != 3:
        choice_1 = 0
        choice_2 = 0
        choice_1 = loop_for_input(choice_1, list_choice_1, 'main')
        if choice_1 == 1:
            while choice_2 != 2:
                choice_2 = 0
                list_choice_2 = [1, 2]
                choice_2 = loop_for_input(choice_2, list_choice_2, 'add')
                if choice_2 == 1:
                    print()
                    question_user = input('Question:\n')
                    while question_user == '' or question_user == ' ':
                        question_user = input('Question:\n')
                    answer_user = input('Answer:\n')
                    while answer_user == '' or answer_user == ' ':
                        answer_user = input('Answer:\n')
                    session.add(Flashcard(question=question_user, answer=answer_user))
                    session.commit()
                    dictionary_flashcard[question_user] = answer_user
        print()
        if choice_1 == 2:
            result_list = session.query(Flashcard).all()
            if not result_list:
                print('There is no flashcard to practice!')
                print()
            else:
                for a in result_list:
                    print(f'Question: {a.question}')
                    print('Please press "y" to see the answer or press "n" to skip:')
                    user_answer = input()
                    while user_answer not in ['y', 'n']:
                        print()
                        print('Please press "y" to see the answer or press "n" to skip:')
                        user_answer = input()
                    if user_answer == 'y':
                        print(f'Answer: {a.answer}')
                        print()
                    elif user_answer == 'n':
                        print()
                        pass

    print('Bye!')


if __name__ == '__main__':
    main()
