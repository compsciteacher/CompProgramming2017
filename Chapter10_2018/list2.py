'''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#HCD
#list review and tuples v.1

'''
Create a list that has your name, birthday (separate day, month, and year), and place of birth
Using a for loop print the whole list
Using index references print "I was born in (place)"
Using index references print "The month was (month)"
Add parent's name
Print new list
'''
def create_list():
    info=['Mr. Davis','4th','December','1979','Liberty, MO']
    for i in info: #use iteration to print all info
        print(i)
    print_info(info)

def print_info(info):

    print('I was born in %s'%info[4]) #index references
    print('The month was %s'%info[2])
    info.append('Sheryl Davis')
    for i in info:
        print(i)


create_list()