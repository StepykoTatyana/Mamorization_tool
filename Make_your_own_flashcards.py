""""A good memorizing tool can boost your short and long-term memory. If you tried to learn a foreign language, you probably know what a flashcard is. It is an excellent device to remember facts. Flashcards alone are not enough, we need a special technique.
Let's create our flashcards first. A flashcard is a piece of paper with a question on one side and the answer on the other. Let's assume we need to memorize the capital cities of various countries. Write the country name on one side and the capital on the other.
In this stage, we need to create our first flashcards.
When the program starts, it should print the menu below. It is our main menu (1):
1. Add flashcards
2. Practice flashcards
3. Exit
If 1 is entered, the program should print the following sub-menu (2):
1. Add a new flashcard
2. Exit
By choosing the Add a new flashcard option, a user is prompted to enter a Question and an Answer. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.

Flashcard practice:
The Practice flashcards option in the main menu (1) should print all the questions and answers that have been added previously. If there are no flashcards, print There is no flashcard to practice! and return to the main menu (1).
Your flashcard should appear on the screen in the following way:
Question: {your question}
Please press "y" to see the answer or press "n" to skip:
If y is entered, the program should output Answer: {your answer} and go to the next flashcard. If there are no flashcards to show, return to the main menu (1).

If n is entered, skip to the next flashcard. If there are no flashcards to show, return to the main menu (1).

Once the program has reached the end of a flashcard list, return to the main menu (1).

Please keep in mind the following:

In case of the wrong input, output the following message: {wrong key} is not an option. Wait for the right input.
Your questions and answers must be non-empty values. Otherwise, wait for the input.
Don't forget about the goodbye message. Output Bye! every time a user exits the program."""


def check_input(input_value, list_check):
    try:
        if int(input_value) in list_check:
            return int(input_value)
        else:
            print(f"{input_value} is not an option")
            return f"{input_value} is not an option"
    except ValueError:
        print(f"{input_value} is not an option")
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
        if choice_1 == 1:
            while choice_2 != 2:
                choice_2 = 0
                list_choice_2 = [1, 2]
                choice_2 = loop_for_input(choice_2, list_choice_2, 'add')
                if choice_2 == 1:
                    print()
                    question = input('Question:\n')
                    while question == '' or question == ' ':
                        question = input('Question:\n')
                    answer = input('Answer:\n')
                    while answer == '' or answer == ' ':
                        answer = input('Answer:\n')
                    dictionary_flashcard[question] = answer
        print()
        if choice_1 == 2:
            print()
            if len(dictionary_flashcard) == 0:
                print('There is no flashcard to practice!')
                print()
            else:
                for q, a in dictionary_flashcard.items():
                    print(f'Question: {q}')
                    print('Please press "y" to see the answer or press "n" to skip:')
                    user_answer = input()
                    if user_answer == 'y':
                        print(f'Answer: {a}')
                        print()
                    elif user_answer == 'n':
                        print()
                        pass
                    else:
                        print(f'{user_answer} is not an option')
    print('Bye!')


if __name__ == '__main__':
    main()
