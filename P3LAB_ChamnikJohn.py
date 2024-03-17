#John Chamnik
#3/16/2024
#P3LAB
#How to write code that displays information to users

input_year = int(input('Enter a year: '))
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False
    
        
if is_leap(input_year):
    print(input_year, ' - leap year')
    
else:
    print(input_year, ' - not a leap year')
