#do all imports at top of program, so everything can use them

import random
import math

def simple_print(): #simple printing of strings and integers
    x=5
    print('I am '+str(x)) #an integer/float must be made a string to print it correctly

def input_example(): #getting inputs, using them. ALL INPUTS ARE STRINGS UNTIL YOU CHANGE THEM
    name=input('What is your name? ')
    age=int(input('How old are you? '))#notice the int before the input!
    number=input('What is the number? ')
    int_number=int(number)#the other way of making an input into a number
    print('Hi '+name+' you are '+str(age)+ ' years old!')

def math_example():#some simple math stuff
    num1=float(input('First number: '))#you can float, int, or anything else to an input to change it's type
    num2=float(input('Second number: '))
    new_num=math.pow(num1,num2)#notice this is a function that takes two parameters
    print(new_num)

def random_example(): #using random module
    first=random.randint(1,11) #again two parameters, starting point and end
    # (remember it is up to second number, not inclusive)
    print("A random number between one and ten is "+str(first))
    second=int(input('What do you want the maximum number to be? '))#I INTEGERED IT!
    second_random=random.randint(1,second)
    print('A random number between 1 and '+str(second)+" is "+str(second_random))

def loop_example():
    total=int(input("How many times should I print it? "))
    phrase=input('What do I print? ')#it is a string so I don't mess with it
    for x in range(total):
        print(str(x)+" times")
        print(phrase)

def conditional_example():
    correct='bob'
    entry=input('What is your name? ')
    if correct==entry:
        print('Hi bob!')
    else:
        print('WHO ARE YOU?!??!?!?! ')
        conditional_example() #recursion, just run it again if they are wrong

def recursion_passing_values(x):
    print('This was passed to it: '+x)
    get_new=input("Now what? ")
    recursion_passing_values(get_new)#runs it again, with whatever is passed to it


#run the functions after defining them
simple_print()
input_example()
math_example()
random_example()
loop_example()
conditional_example()
recursion_passing_values('lkasjdf;ljsa')