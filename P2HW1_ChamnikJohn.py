#John
#2/29/2024
#P2HW1
#Assignment assess student ability to edit and enhance exiting programs

budget = float(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas? '))
accommodation = float(input('Approximately, how much will you need for accommodation/hotel? '))
food = float(input('Last, how much do you need for food? '))
print('------------Travel Expenses------------')
print('Location: ', destination)
print(f'Initial Budget:    ${budget:.2f}')
print(f'Fuel:              ${gas:.2f}')
print(f'Accommodation:     ${accommodation:.2f}')
print(f'Food:              ${food:.2f}')
print('---------------------------------------')
expenses = (gas+accommodation+food)
balance = (budget-expenses)
print(f'Remaining Balance: ${balance:.2f}')
