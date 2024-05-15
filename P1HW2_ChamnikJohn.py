#John
#2/20/2024
#P1HW2
#Create a program that does some basic math on numbers that are entered

'''
Created user inputs using integer function with prompt for for the budget, destination, gas, accommodation, and food.
Used the print function to display each variable.
Added the expenses together to get a total and then subtracted the expenses from the budget to get the remaining balance.
'''

budget = int(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
accommodation = int(input('Approximately, how much will you need for accommodation/hotel? '))
food = int(input('Last, how much do you need for food? '))
print('----------Travel Expenses----------')
print('Location: ',destination)
print('Initial Budget: ',budget)
print('Fuel: ',gas)
print('Accommodation: ',accommodation)
print('Food: ',food)
expenses = (gas+accommodation+food)
balance = (budget-expenses)
print('Remaining Balance: ',balance)
