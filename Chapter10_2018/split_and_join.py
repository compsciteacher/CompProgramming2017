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
#Split/Join v.1

'''
split_and_join.py
Have this string:
"My name is Jose"
Split string into a list based on spaces
PRINT
Then:
"user1;user2;user3"
Split string into a list with ; as the parameter
PRINT
Join the following list using " " as the glue
['this','is,'a','sentence']
PRINT
'''

def sent_split(): #splitting sentence to a list
    sent="My name is Jose"
    sent_split_up=sent.split()
    print(sent_split_up)

def split_it_semicolon(): #splitting users to a list based on ;
    together='user1;user2;user3'
    split_up=together.split(';')
    print(split_up)

def glue_it(): #glueing list into a single string
    sent_list=['this','is','a','sentence']
    glued=' '.join(sent_list)
    print(glued)

#run defined functions
sent_split()
split_it_semicolon()
glue_it()
print('----------------------------------------------')


#another option with passing
#see above functions, but I am sending the objects instead of defining in functions, the returning results
def sent_split2(sent):

    sent_split_up=sent.split()
    return sent_split_up

def split_it_semicolon2(together):

    split_up=together.split(';')
    return split_up

def glue_it2(sent_list):

    glued=' '.join(sent_list)
    return glued


#running functions and printing returned results
print(sent_split2("My name is Jose"))
print(split_it_semicolon2('user1;user2;user3'))
print(glue_it2(['this','is','a','sentence']))