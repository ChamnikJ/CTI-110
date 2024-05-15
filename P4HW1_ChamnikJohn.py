#John Chamnik
#4/9/2024
#P4HW1
#Edit and enhance exiting programs

num_scores = int(input('How many scores do you want to enter? '))
score_list = []

for i in range(num_scores):
    score = float(input(f'Enter score #{i+1}:'))
    while score < 0 or score > 100:
        print('INVALID Score entered!!!')
        print('Score should be between 0 and 100')
        score = float(input(f'Enter score #{i+1}:'))
    score_list.append(score)
print()
print()
print('------------------Results------------------')
score_low = min(score_list)
print(f'Lowest Score    : {score_low} ')
score_list.remove(score_low)
print(f'Modified List   : {score_list} ')
score_avg = sum(score_list)/len(score_list)
print(f'Scores Average  : {score_avg:.2f} ')

if score_avg >=90:
    grade = ('A')
elif score_avg >=80:
    grade = ('B')
elif score_avg >=70:
    grade = ('C')
elif score_avg >=60:
    grade = ('D')
else:
    grade = ('F')
print(f'Grade           : {grade}')
print('-------------------------------------------')
    







    

