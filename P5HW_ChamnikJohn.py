#John Chamnik
#4/28/2024
#P5HW

import random
number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
    
def display_intro():
    print('Welcome to Math Quiz')
    print()
    print()
    print('MAIN MENU')
    print('-------------------------')
    
def display_menu():
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit\n')
    print()
    
def get_user_input():
    user_input = int(input('Please choose one of the menu option: '))
    while user_input > 3 or user_input <= 0:
        print('Invalid option.')
        user_input = int(input('Try again: '))
    else:
        return user_input

def get_user_solution(problem):
    print(problem, end='')
    result = int(input('='))
    return result

def check_solution(user_solution, solution, count):
    while user_solution != solution:
        count = count + 1
        if user_solution > solution:
            print('Sorry, guess is too high.')
        if user_solution < solution:
            print('Sorry, guess is too low.')
        user_solution = int(input('Try again: '))
    print('Congratulation!!!! Your answer is correct.')
    print(f' Number of guesses: {count}')


def menu_option(index, count):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    if index is 1:
        problem = str(number1) + '+' + str(number2)
        solution = number1 + number2
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, 1)
        return count
    elif index is 2:
        problem = str(number1) + '-' + str(number2)
        solution = number1 - number2
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, 1)
        return count
    elif index is 3:
        print('Thank you for playing...')
        print('Bye!!!')

def main():
    display_intro()
    display_menu()

    option = get_user_input()
    correct = 1
    while option != 3:
        correct = menu_option(option, correct)
        option = get_user_input()

    print('Thank you for playing...')
    print('Bye!!!')

main()



