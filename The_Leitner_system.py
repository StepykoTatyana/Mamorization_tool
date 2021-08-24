#5/5
"""Description
We know how to create flashcards, but it is not enough. At the beginning of the project, we mentioned a special technique that can help us with our task of creating a useful memorizing tool. Don't worry, we are about to take off and our flashcards will help. We are going to implement the Leitner system in our program. In short, it introduces the concept of spaced repetition proposed by Sebastian Leitner, a German scientist. Leitner's system suggests reviewing cards at increased intervals.
We can divide the memorization process into several parts. First, you create several boxes (usually from 3 to 5) that will store your flashcards. You mark each box with time periods that show how frequently the cards should be reviewed. For example, Box 1 will contain the most difficult cards, so they should be reviewed every day; Box 2 will have easier cards that you will check more rarely, every two days, and so on.
Next, you start learning and arranging the flashcards. You go through multiple Sessions. During Session 1, all your cards are in Box 1. You answer questions on these cards. If you are right, the card moves to Box 2 — that means that you don't need to repeat the information on the card so often. If your answer is wrong, your card stays in Box 1 — that means that you will see this card more frequently. When you reach Session 2, you answer questions on the cards both in Box 1 and Box 2. During Session 3, you study the cards in all three boxes. Again, every time you get a card wrong, you move it to Box 1. If you get the card right, you move it to the next box.
In this stage, there are three boxes, and if you give the correct answers to the cards in the third box, it means you've learned them, and you don't need those cards anymore, so you can remove them from the database.

If you want to read about this method in a little more detail, refer to the MindEdge article.
Objectives
After displaying each question, you need to ask users whether their answers are correct or not. To do this we need to create another menu, let's call it the learning menu (5):

press "y" if your answer is correct:
press "n" if your answer is wrong:
This will correspond to Session 1 for these cards. New flashcards and cards with wrong answers should go to the first box. Once you reach Session 3 for them, you can remove them from the database.

A good idea would be to add a column that will stand for the "box number". When a new flashcard is created, set it to some value, and update it once the user answers the card correctly during practicing.

Output the <wrong key> is not an option message when a user presses the wrong key. Other parts of the program should operate as in the previous stages.
"""

from create_db import engine, Flashcard
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
            print()
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


def check_answer(a):
    print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
    user_check = input()
    while user_check not in ['y', 'n']:
        print()
        print(f'{user_check} is not an option')
        print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
        user_check = input()
    if user_check == 'y':
        if a.box == 1:
            a.box = 2
            session.commit()
        elif a.box == 2:
            a.box = 3
            session.commit()
        elif a.box == 3:
            session.delete(a)
            session.commit()
    elif user_check == 'n':
        if a.box == 2:
            a.box = 1
            session.commit()
        elif a.box == 3:
            a.box = 1
            session.commit()


def main():
    # dictionary_flashcard = {}
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
                    session.add(Flashcard(question=question_user, answer=answer_user, box=1))
                    session.commit()
                    # dictionary_flashcard[question_user] = answer_user
                print()
        if choice_1 == 2:
            result_list = session.query(Flashcard).all()
            if not result_list:
                print('There is no flashcard to practice!')
                print()
            else:
                for a in result_list:
                    print()
                    print(f'Question: {a.question}')
                    print('press "y" to see the answer:')
                    print('press "n" to skip:')
                    print('press "u" to update:')
                    user_answer = input()
                    while user_answer not in ['y', 'n', 'u']:
                        print()
                        print(f'{user_answer} is not an option')
                        print('press "y" to see the answer:')
                        print('press "n" to skip:')
                        print('press "u" to update:')
                        user_answer = input()
                    print()
                    if user_answer == 'y':
                        print(f'Answer: {a.answer}')
                        check_answer(a)
                    elif user_answer == 'n':
                        check_answer(a)
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

