first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))

if first == second and first == third:
    print('All', 3, 'numbers are equal to each other')
elif first == second or first == third or second == third:
    print(2, 'numbers are equal to each other')
else:
    print('Detected', int(not 1), 'numbers that are equal to each other')
