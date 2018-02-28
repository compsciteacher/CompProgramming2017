import time, getpass, sys, argparse
'''
User login program that includes:
Simple user login using a logins.txt file
An administration login with separate admin_logins.txt file
Ability to create users, delete users, and change passwords.
Log that keep tracks of ALL logins including failures

Login Program v.3
Mr. Davis
2/27/18
'''
def main_menu(): #currently has regular login that logs date/time/success, admin login that logs same data, and quit
    choice=input('''
    1 Login
    2 Administration
    3 Quit
    : ''')
    if choice=='1':
        login(3,'logins.txt') #runs login with regular login file
    elif choice=='2':
        login(3,'admin_logins.txt') #runs login with an admin login file
    elif choice=='3':
        quit()
    else: #catch all
        print('Invalid Entry')
        main_menu()
def admin_menu(): #allows admin to create users, delete users
    choice=input('''
    1 Create User
    2 Delete User
    3 Change Password
    4 Main Menu
    : ''')
    if choice=='1':
        create_user()
    elif choice=='2':
        delete_user()
    elif choice=='3':
        changepw()
    elif choice=='4':
        main_menu()
    else:
        print('Invalid Entry')
        admin_menu()
def changepw():
    loginfile='logins.txt'
    user = input('Which user to change password: ')
    if user=='admin': #change to admin users if they say change admin pw
        loginfile='admin_logins.txt'
    user_pws = open(loginfile, 'r')  # read current users
    output = []# creates temporary output variable
    notfound=True #this will determine if the user they enter is found in the file, starts with not found
    for line in user_pws:
        linelist = line.split() # makes each line into a list
        if user==linelist[0]: #user found
            notfound=False
            newpw=input('What is the new password? ')
            linelist[1]=' '+newpw #have to put the space so that the new string has that to split un and pass
            changed='' #new user and pw string
            for x in linelist:
                changed+=x
            output.append(changed) #add the user and pw to output


        if user != linelist[0]:  # checks line, if it is not equal to user then adds to output
            output.append(line)
    if notfound==True: #if the user entered is not found, then give error and ask again (OOPS! THEY COULD GET INFINITE LOOP,
        #so now if user not found go to admin menu
        print('USER NOT FOUND!')
        user_pws.close()
        admin_menu()
    user_pws.close()  # closes old file after reading it
    newfile = open(loginfile, 'w')  # creates new file, write the temp output variable
    for x in output:
        newfile.write(x)
    newfile.close()
    admin_menu()
def login(attempts,userlist): #user attempts to login, only has 3 attempts to start. can use different user lists
    users_pws=open(userlist,'r') #user/pw file
    print("Welcome, please login")
    usern_entry=input('User: ')
    userp_entry=getpass.getpass("Password: ")
    for i in users_pws:
        check=i.split() #turns line into string to check, using 'x in y' check would come True even if username was password
        if usern_entry==check[0]:
            if userp_entry==check[1]:
                print("Successful login")
                logger(usern_entry,userp_entry,"Successful") #logs username,pw entered, success, and date/time
                if userlist=='admin_logins.txt': #if it is the admin list, with success go to admin menu
                    admin_menu()
                time.sleep(2)
                main_menu() #for now on success it let's user know then goes back to main menu

    print("INCORRECT USERNAME OR PASSWORD")
    logger(usern_entry,userp_entry,"Unsuccessful") #logs username, pw entered, unsuccessful, date/time
    attempts-=1 #only allow 3 attempts, so subtract one try each time, then check number remaining, at 0 quit
    if attempts==0:
        print("LOCKED OUT")
        time.sleep(2)
        quit()
    login(attempts,userlist) #if attempts is !=0 then it runs login with new attempt number same file as before

def logger(x,y,z): #username, userpassword,success or not
    ts = time.gmtime()
    time_formatted=time.strftime("%Y-%m-%d %H:%M:%S", ts)
    loggerfile=open('logs.txt','a')
    loggerfile.write("%s %s %s %s \n" %(x,y,z,time_formatted))
    loggerfile.close()

def create_user():  #admin creates a user
    newuser=input('User to create: ')
    if ' ' in newuser: #makes sure there are no spaces in username
        print('Cannot have a space in username')
        create_user()
    users_pws = open('logins.txt', 'r')# user/pw file
    for userline in users_pws: #checks to see if user exists, if it does it will just run create again
        if newuser==userline.split()[0]:
            print('User already exists')
            users_pws.close()
            admin_menu()
    users_pws.close() #new user does not currently exist in file, so closes
    newpw=input('Password: ')
    created=newuser+' '+newpw
    user_add_file=open('logins.txt','a') #opens login file with append privilges
    user_add_file.write(created+'\n')
    user_add_file.close()
    print('%s created!'%newuser)
    admin_menu()
def delete_user():
    user=input('Which user to delete: ')
    user_pws=open('logins.txt','r') #read current users
    output=[] #creates temporary output variable
    for line in user_pws:
        linelist=line.split() #makes each line into a list
        if user!=linelist[0]: #checks line, if it is not equal to user then adds to new output
            output.append(line)
    user_pws.close() #closes old file after reading it
    newfile=open('logins.txt','w') #creates new file, write the temp output variable
    for x in output:
        newfile.write(x)
    newfile.close()
    admin_menu()

main_menu()