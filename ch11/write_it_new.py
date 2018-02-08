# write_it.py
# Create 10 random numbers that are 7 digits long (MUST BE 7 DIGITS!)
# Write those numbers to a file called "numbers.txt"
# Close the file

#HCD Write It 2/8/18
import random

def write_it(f):
    file=open(f,'w')
    for i in range(10):
        strnum=''
        for x in range(7):
            num=random.randint(0,9)
            strnum+=str(num)
        file.write(strnum+'\n')


    file.close()
    print('task complete')

write_it('numbers.txt')