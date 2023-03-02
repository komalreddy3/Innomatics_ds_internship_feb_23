"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
"""

x=int(input())
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
list=[]
for i in range(x):
    num=input()
    if len(num)==10 and num.isalnum() is True:
        for i in range(10):
                list.append(num[i])
    l=0
    m=0
    for j in range(len(list)):
       for k in range(len(upper)):
         if list[j]==upper[k]:
            l+=1
    for q in range(len(list)):
       for r in range(len(digits)):
          if list[q]==digits[r]:
            m+=1
    seen=[]
    for n in range(len(list)):
        if list.count(list[n])>1:
            seen.append(list[n])
    if l>=2 and m>=3 and len(seen)==0:
        print("Valid")
    else:
        print("Invalid")
    list=[]
