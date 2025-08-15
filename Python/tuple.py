'''Basic Concept and syntax'''
#1 created a tuple containing 5 colours and printing 2nd and 4th using indexing
color=('red','blue','green','black','grey')
print(color[1],color[3])

#2 created a tuple with single element and printed its type using type() function
num=(1)
print(type(num))

#3 converting a list into tuple using tuple() function
fruit=['apple','banana','cherry']
new_fruit=tuple(fruit)
print(new_fruit)

#4 created 2 tuples and concatinated both 
num1=(1,2,3)
num2=(4,5,6)
print(num1+num2)

#5 
lan=('python','java','c++')
if 'python' in lan:
    print('python exists in tuple')
else:
    print('python does not exists in  tuple')


    '''Medium'''
#1 unpacking the tuple in 4 varibales
nums=(10,20,30,40)
a,b,c,d=nums
print(a,b,c,d)

#2 finding the index of 5
numm=(1,5,7,5,9 )
new=numm.index(5)  
print(new)

#3 slicing the tuple to print bcd 
t=('a','b','c','d','e')
print(t[1:4])

#4 counting how many times 2 appears in tuple using .count method
even=(2,4,2,6,2,9)
print(even.count(2))

#5 merging 2 tuple into 1 and sorting them 
a=(1,2,3,4,5)
b=(6,7,9,8)
c=(a+b)
print(sorted(c))

'''challenging'''
#1 removing an element in tuple by converting it into new list and removing the element and converting that list into tuple
p=(1,2,3,4,5,6)
element_to_remove=3
temp_list=list(p)
temp_list.remove(element_to_remove)
new_tup=tuple(temp_list)
print(new_tup)

#2 converting a tuple into dictonary
u=(('a',1),('b',2),('c',3),)
print(u)
new_u=dict(u)
print(new_u)

#3
t1=(1,2)
t2=(3,4)
t1,t2=t2,t1
print(t1)
print(t2)

#4 reversing the tuple without using slicing
t3=(1,2,3,4,5,6)
temp_tup=list(t3)
temp_tup.reverse()
reversed_t3=tuple(temp_tup)
print(reversed_t3)

#5
user=tuple(input("Enter multiple elements:"))
print(user) 




