#Your info

'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.'''

'''Create a password requirement checker:
Tell the user their password must be 8 characters long, include one special character (!,@#$%^&*.?),
include at least one capital letter, and not include the words "pass" "word" or "default"
Ask the user for an input
Check to see if it meets the requirements'''

def username(): #this is to get username for new user
    print("Let's create an account!")
    un=input("What is your username? ")
    #check_inventory(un) <--- this will check the user's entry against existing names
    pass_check(un)

def pass_check(name): #this will check to see if their password will meet requirements
    print("Your username is %s" %name)
    #here is your code

username()