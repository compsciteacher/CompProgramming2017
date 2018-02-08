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
#in class lists


'''
names=Create a list with 5 names
numbers=Create another list with 5 double digit numbers
both=Create a list that puts these two lists into one
squeezed=Squeeze 2 new names into the list of names (don't care where, but not at the beginning or end) <--- this shows me you understand the 'squeeze' process

Print all the lists
'''
def create_list():

    names=['bob','jenny','jill','frank','lee']
    print(names)
    numbers=[1,2,3,4,5]
    print(numbers)
    both=names+numbers #concatenate lists
    print(both)
    names.insert(1,'chris') #squeeze or insert the 2 new names
    names.insert(2,'shanna')
    print(names)

create_list()