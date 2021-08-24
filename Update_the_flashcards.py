# 3/4
"""Different Query object methods can give access to the table entries. The all() method returns a list of all table entries, update({<mapped class attribute>:<new value>}) replaces the existing value with a new value, delete() deletes query results. Take a look at how some of the methods can be applied:
entries = session.query(Database).all()  # get all table entries
entry = entries[0]

# the following lines update the entry
entry.value = 10
session.commit()

# the following lines delete the entry
session.delete(entry)
session.commit()
There are also such useful methods as get(<primary key value>) that returns an entry based on the given primary key, and filter(<criteria>) that returns only those entries that match the given criteria.

Description
In this stage, we are going to add new features to our program. For example, we may need to edit or get rid of some flashcards.

Objectives
We need to add new features to the menu that comes up once a user entered the Practice flashcards key from the previous stage. Let's call it the practice menu (3):

press "y" to see the answer:
press "n" to skip:
press "u" to update:
As you can see, it still contains the y and n options. A user advances to another menu by entering u. Let's call it the update menu (4).

press "d" to delete the flashcard:
press "e" to edit the flashcard:
d deletes a flashcard, the e option offers a way to edit the current flashcard. First, we need to edit the question:

current question: <question>
please write a new question:
Once the question has been edited, proceed to the answer:

current answer: <answer>
please write a new answer:
If the user leaves the question or the answer field empty, keep the original question or answer value unchanged.

Output the <wrong key> is not an option message in both practice (3) and update (4) menus when a user presses the wrong key. Other parts of the program should operate as in the previous stages.

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
            print()
            print(f"{input_value} is not an option")
            return f"{input_value} is not an option"
    except ValueError:
        print()
        print(f"{input_value} is not an option")
        print()
        return f"{input_value} is not an option"


def print_main_menu():
    print('1. Add flashcards')
    print('2. Practice flashcards')
    print('3. Exit')


def print_add_menu():
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
        print()
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
                    print('press "y" to see the answer:')
                    print('press "n" to skip:')
                    print('press "u" to update:')
                    user_answer = input()
                    while user_answer not in ['y', 'n', 'u']:
                        print(f'{user_answer} is not an option')
                        print('press "y" to see the answer:')
                        print('press "n" to skip:')
                        print('press "u" to update:')
                        user_answer = input()
                    if user_answer == 'y':
                        print(f'Answer: {a.answer}')
                    elif user_answer == 'n':
                        pass
                    elif user_answer == 'u':
                        print('press "d" to delete the flashcard:')
                        print('press "e" to edit the flashcard:')
                        user_answer = input()
                        while user_answer not in ['d', 'e']:
                            print(f'{user_answer} is not an option')
                            print('press "d" to delete the flashcard:')
                            print('press "e" to edit the flashcard:')
                            user_answer = input()
                        if user_answer == 'd':
                            session.delete(a)
                            session.commit()
                        elif user_answer == 'e':
                            print()
                            print(f'current question: {a.question}')
                            print('please write a new question:')
                            user_new_question = input()
                            if user_new_question == '' or user_new_question == ' ':
                                pass
                            else:
                                a.question = user_new_question
                                session.commit()
                            print()
                            print(f'current answer: {a.answer}')
                            print('please write a new answer:')
                            user_new_answer = input()
                            if user_new_answer == '' or user_new_answer == ' ':
                                pass
                            else:
                                a.answer = user_new_answer
                                session.commit()
                    print()
    print('Bye!')


if __name__ == '__main__':
    main()
