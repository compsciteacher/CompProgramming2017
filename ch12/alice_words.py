
def biggest_word(book):
    f=open(book,'r')
    word_lengths={} #dictionary with word and length
    full_book=f.read()
    full_list=full_book.split() #gives all words in a list
    for word in full_list: #iterates over words
        word_lengths[word]=len(word) #makes the word the key, length the value, adds to word_lengths dictionary
    max_word='' #start with no word as max
    max_value=0 #start with max value as 0

    #this is a complicated way, but cleaner/shorter
    # k=list(word_lengths.keys())
    # v=list(word_lengths.values())
    # print(k[v.index(max(v))]+' is '+str(max(v))+' characters long.')
    #it finds the index of the max value, then uses that index to get the key from the key list

    #simple iteration
    for i in word_lengths:
        if word_lengths[i]>max_value: #checks if length of key is bigger than current max, if it is makes the max values match
            max_value=word_lengths[i]
            max_word=i
    print(max_word)
    print(max_value)




biggest_word('alice.txt')
