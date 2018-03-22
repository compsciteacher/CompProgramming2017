def ask_word():
    entry=input('Give a word: ') #get word that is passed to the index asking
    check(entry)
def check(entry):
    try:
        x=float(input('What index value of the word would you like to show: ')) #get number for index
        if 0<=x<len(entry): #checks to see if it is 0 to the length of word (not including length)
            print(entry[int(x)]) #print the character that matches index value of the word

        else:
            print('Number outside valid range') #index value they give is outside range, run just the number ask
            check(entry)
    except ValueError: #only if they don't enter a number
        print('Must give whole number between 0 and length of word ')
        check(entry) #runs number check again, doesn't ask for word again

ask_word()