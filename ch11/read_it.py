

#in class reading files

def read_it():
    file1=open('students.txt','r')

    line=file1.readline()
    while line:
        print(line)
        line=file1.readline()



    file1.close()


read_it()
