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
#My list (list review) v.1

'''Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Do it with both append and
with concatenation, one item at a time.
Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average.

'''
import random
def create_list():
    myList=[] #empty list to start with, then using append to add necessary items one at a time
    myList.append(76)
    myList.append(92.3)
    myList.append('hello')
    myList.append(True)
    myList.append(4)
    myList.append(76)
    print(myList)
    #a different way of doing for it
    myList2=[]
    for i in (76, 92.3, 'hello', True, 4, 76): #using iteration to add each item
        myList2.append(i)
    print(myList2)

    #using concatenation
    myList3=[]
    myList3+=[76]
    myList3+=[92.3]
    myList3+=['hello']
    myList3+=[True]
    myList3+=[4]
    myList3+=[76]
    print(myList3)

def rand_num_list():
    nums=[] #empty list of numbers
    for i in range(100):
        x=random.randint(0,1000) #create the random number, then append to list
        nums.append(x)
    print(nums)
    sum=0
    for i in nums:
        sum+=i #go through list of numbers and add to the total sum
    avg=sum/100 #get average
    return avg #return that final average

create_list()
print(rand_num_list()) #notice I only printed the returned value, I didn't make it a variable or anything