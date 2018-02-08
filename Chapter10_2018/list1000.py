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



x=['a']
def names(x):
    print(x)
    new=input('Name to add: ?')
    x.append(new)
    #print(x) <--- again was for debugging
    again=input('Another name to add?')
    if again=='y':
        names(x)
    elif again=='n':
        #print(x) <-- this was to debug
        print('Full list: ')
    else:
        print('Error')
        names(x)
    return x
y=(names(x))
print(y) #just printing right now, but want to be able to do stuff with names list outside the function