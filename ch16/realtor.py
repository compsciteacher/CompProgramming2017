import math
import time

ALL_BUYERS=[] #will keep a list of all buyers
ALL_HOMES=[] #for later

class House: #House object that will have address, rooms, squre feet, and budget
    def __init__(self,initAddress,initRooms,initSquare_feet,initPrice):
        self.address=initAddress
        self.rooms=initRooms
        self.square=initSquare_feet
        self.price=initPrice

    def print_address(self): #will only print address
        return self.address
    def cost_per_sqft(self): #print only square feet
        return (self.price/self.square)
    def __str__(self): #string method will print address and price
        return ("The address is %s and the price is %s"%(self.address, str(self.price)))

class Buyer: #Buyer class that will have first name, last, phone, number of rooms buyer wants, and their budget
    def __init__(self,first,last,phone, minimum_rooms,budget):
        self.first=first
        self.last=last
        self.phone=phone
        self.minimum_rooms=minimum_rooms
        self.budget=budget
    def __str__(self): #string method will print a well formatted sentence about buyer
        return("%s %s is looking for a home that costs %s"%(self.first,self.last,self.budget))

def buyer_entry(): #as we get new buyers this will ask for info and pass to object creation
    global ALL_BUYERS #will keep track of each buyer as they are entered
    f=input('First name: ')
    l=input('Last name: ')
    p=input('Phone number: ')

    try:
        m = int(input('Minimum number of rooms needed: '))
        b= int(input("Buyer's maximum budget: "))

    except (ValueError): #catches multiple errors, took awhile to get correct
        print("Number of rooms and budget must be numerical values")
        buyer_entry()

    ALL_BUYERS.append(Buyer(f,l,p,m,b)) #creates Buyer object with info entered
    menu()

def menu(): #asks for creation of new buyers, homes, and eventually checking for appropriate homes
    global ALL_BUYERS #called only for debugging code below
    print('''
    1. New Buyer
    2. New House
    3. Find House
    ''')
    choice=input(": ")
    if choice=='1':
        buyer_entry()
    elif choice=='2':
        pass
    elif choice=='3':
        pass
    elif choice=='4':
        for x in ALL_BUYERS:
            print(x)
        menu()
    else:
        print('Incorrect entry, please enter a number only')
        menu()



menu()
