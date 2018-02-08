#append or concatenate?


#create list with function
def new_list(name):#getting dudet
    users=['bob','jenny','jill','jet']
    users.append(name)
    return users #bob,jenny,jill,jet,dudet


    #how do I add new user?


def list_pass(oldlist):
    oldlist.append('bob')
    return oldlist

all_names=new_list('dudet')
print(names)
print(list_pass(['jenny']))







mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)