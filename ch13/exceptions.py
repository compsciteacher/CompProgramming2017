def asking():
    try:
        x=float(input('Give a whole number between 1 and 10: ')) #get the number
        if 1<=x<=10: #check range of number, if you give 0<x<=10, would be a valid number

            print(int(x)) #prints the whole number after int it
        else:
            print('Number outside valid range') #if it doesn't meet valid range of 1 to 10 run again
            asking()
    except ValueError: #if they don't enter a number, only checks that they did a number
        print('Must give whole number between 1 and 10')
        asking() #run again for error
asking()