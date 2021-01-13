#import random

#number = random.randint (1,10)
#print (number)

print('Hello World!')

name = 'Johanna'

x = 4

#for i in range(10):
 #   print(i)

number = 5/3
print(number)

#for i in range(9):
 #   row= i//3
  #  column= i%3
   # print (row,column)

print('hello ' *3) 
text= 'hello'

boolean = text == 'hello'
print(boolean)



a=3
b=9
print(a>=b)

print(a>1 and b>2)

print((a>1 or b>1) and (a<5 or b<1))

if a>2: #if this is true, it'll print the statement
    print('Hi')

print(input('whatever you ask the user here')

# password = input('what is the password?') 
# print(password)

# if password == '123456':
#     print('Top secret information!')
# else:
#     print('You shall not pass')

# passcode = input('what is the password?')
# passcode = float(passcode)
# #makes sure that the code is an integer, does casting, which converts a value into something(i.e an integer or a floating number)

# while passcode != 123456:
#     passcode = input('What is the password?')
#     passcode= float(passcode)
# print('Top secret information!')

#if passcode == 123456:
 #   print('Top secret information')
#so any passcodes that is not an integer (or floating point) will be false

# a= int(15/3)
# print('Hello ' + str(a))

#print('hello'.upper())

print(len('I am yelling'))

print('5'.isnumeric())
#evaluates if the string is numeric
x= input('Please enter a number:')
if x.isnumeric():
    print('I am filled with gratitude for the numeric input you have provided!')
else:
    print('It looks like you entered something which is not a number...')

x=input('How old do you turn this year?')
if x.isnumeric():
    print(f'You were born in:{2021-x}')
else:
    print('Invalid input!')

# print('hello world'.count('l'))
# print('hello world'.index('l'))
print(' hello world   '.strip())
# print (f'Hello{a}')

print(len(word_salad.replace(' and another word ', '.')))

print('Goodbye' not in 'GoodBye') #says that the first is not included in the secon
print((('American' not in 'American') and 4.6 != 3.2) and (('response' not in 'response') and 9.9>9.9))

for i in range(3, 44, 6):
    print(i)
#second, is the step size!

counter = counter + 1 #to add numbers to a variable i guess

# Using a while loop and the `.count()` method of the following string, given to you as the variable `input_string`, reduce the number of nots to the smallest number that still carries the same meaning, and print the result to the terminal: "I wil not not not not not not not not accomodate management"
while input_string.count('not not ')>0:
    input_string= input_string.replace('not not ', '')
print(input_string)

num=10
while num <46:
    print(num)
    num= num+4


counter=0
while 0<=counter<=10:
    print(f'I have seen {counter} porcupines')
    counter=counter+1

#working option shit!
guess=101

while guess!=value:
    guess= input('Guess? ')
    if guess.isnumeric():
        guess=int(guess)
        if 0<=guess<=100:
            if guess<value:
                print('Incorrect, higher!')
            if guess>value:
                print('Incorrect, lower!')
        else: 
            print('Invalid input!')
    else:
        print('Invalid input!')
print('Correct!')    