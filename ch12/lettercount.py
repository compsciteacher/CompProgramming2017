

def letter_count(sentence):
    num_letters={}
    letters = num_letters.keys()
    for ch in sentence:
        if ch in letters:
            num_letters[ch]+=1
        else:
            num_letters[ch]=1
    print(num_letters)
countit=input('What sentence do you want the letters counted? ')
letter_count(countit)
