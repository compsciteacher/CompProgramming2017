


def uhoh(word):
    entry=input('Word? ')
    if entry!=word:
        uhoh(word)
    print('yay')

uhoh('cat')