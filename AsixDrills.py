'''
Created on Apr 25, 2020

@author: ITAUser
'''

from asyncio.__main__ import loop
'''
For these drills you will be making functions that use all of the
skills we've covered in the units so far. This includes variables,
math operators, comparison operators, conditional statements, loops,
and functions.

'''


'''
1) Make a function that takes two parameters: a list(list), 
and a string(name).
In the function you should make a loop that runs through the list,
and check if the name is in the list. If the name is in the list,
return the name. If the name isn't in the list, return "no".

Once done making the function, make a list of five names, and 
a string variable storing another name.
Then call your function, putting in these two variables as the
parameters.
Finally, store what your function returns in another variable and
print out that variable.
'''

#WRITE CODE HERE (OUTSIDE THE COMMENTS)
def name_inside_list(name, nameList):
    #make a loop that will go through the list
        #check if name == items
            #if it is true return name
    #if  name and items are not equal 
    #return "no"
    A = ("Ali", "Alejandra", "Abby")
    
    B = ("Bryce")
    
    if(A == B):
        print(B)
    else:
        print("no")
return 

b = name_inside_list
print(b)
'''
2) Make a function that calculates the Pythagorean theorem for 
one side of a right triangle.

The Pythagorean Theorem is:

a**2 + b**2 = c**2

You will also need the sqrt() function. Here is an example:
print(sqrt(4))
The computer would print(it looks weird but it's just 2):
(2+0j)
This can also be stored in variables like:
x = sqrt(4)

You must also copy paste the following line to the top of you code:
from cmath import sqrt

Your function should take two parameters(a and b). Then the function
should solve for c. Once solved, you should return c.

Once done making the function, make two variables for the two
sides of the triangle.
Then call your function, putting in these two variables as the
parameters.
Finally, store what your function returns in another variable and
print out that variable.
'''

#WRITE CODE HERE (OUTSIDE THE COMMENTS)
from cmath import sqrt
def pythagorean_theorem(a,b):
    
    solvingTheorum = (sqrt(a**2 + b**2))
    return solvingTheorem

c = pythagorean_theorem(20, 50)
print (c)
'''
3) Make a list that stores 5 integers. Store the following numbers:
25, 55, 65, 70, 80, 90, and 100. Name this list grades.
This list will represent a 7 students grades.

Then, make a function that will check each students grade and print
whether they are passing: 80-100, on probation: 60-80, or failing:
0-60.

The function will have one parameter, which is the grade list. And
the function will return the number of students passing.

Call your function, using the grades list you made as the 
parameter.
Finally, store what your function returns in another variable and
print out that variable.
'''

#WRITE CODE HERE (OUTSIDE THE COMMENT
grades = [25, 55, 65, 70, 80, 90, 100]

def func(list):
    for x in list:
        if(x >= 80):
            print("passing")
        elif(x < 80 and x >= 60):
            print("probation")
        elif(x <= 60):
            print("failing")
    return 

p = grades("passing")
print(p)