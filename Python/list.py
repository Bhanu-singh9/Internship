'''1.create list of 5 fav movies'''
movies=["avatar","agent47","black panther","Avengers:End Game","Oppenhiemeir"]
print(movies)

#2.adding all the data types in the list
mixed=[1,2.5,"name",34,"fox"]
print(mixed)

#3 nested list(list inside another list)
nest=['animal','human','plants',['cat','dog','cow']]
print(nest)

#4 accessing firs element of a list(accesing first element of list using indexing)
first=['apple','banana','mango','pineapple','litchi']
print(first[0])

#5 accessing middle element of list using indexing
print(first[2])

#6 accessing last element of list using indexing
print(first[-1])

#7 using negative indexing to list second last element
print(first[-2])

#8 using slicing to print first 3 letter in a list
print(first[0:3])

#9 using slicing to print last 3 letter in a list 
print(first[2:5])

#10 reversing a list using slicing(using negative indexing and reversing it )
print(first[::-1])

#11 replacing the second element of a list using indexing
first[1]=("python")
print(first)

#12 putting the last and second last index and replacing it
first[3]="Done"
first[4]="Finish"
print(first)

#13 concatinating two lists using concatination func
second=['cabbage','cauliflower','tomato']
print(first+second)

#14 repeating a list
print(first*3)

#15 checking if the apple is in the list or not using in operator
print("apple" in first)


'''2 List Methods'''
numbers=[5,2,9,1,5,6]
fruits=['apple','banana','cherry']
#1 adding orange to fruits using .append() method
fruits.append('orange')
print(fruits)

#2 inserting  new element in list using index(inser the index first and then the element you want to add)
fruits.insert(1,"kiwi")
print(fruits)

#3 removing banana from fruits using .remove method
fruits.remove("banana")
print(fruits)

#4 poping last item from numbers using .pop() method.
numbers.pop(-1)
print(numbers)

#5 clearing all the elements from a copy of fruits
print(fruits)
fruits_copy=fruits.copy()
fruits_copy.clear()
print(fruits_copy)

#6 sorting all the elements in ascending order from numbers using .sort() method
numbers.sort()
print(numbers)
 
#7 sorting all the elements in desceding order from numbers using .sort(reverse ) method
numbers.sort(reverse=True)
print(numbers)

#8 reversing the elements of fruit without using sorting (with using slicing)
print(fruits)
print(fruits[::-1])

#9 sorting fruits alphabetically using .sort()
fruits.sort()
print(fruits)

#10 counting how many times 5 appears in numbers using .count method
print(numbers.count(5))

#11 finding index of cherry using .index() method
print(fruits.index("cherry"))

#12 creating shallow copy of nnumbers and modifying it.
print(numbers)
numbers_copy=numbers.copy()
numbers_copy.insert(1,0)
print(numbers_copy)
print(numbers)


'''3. Mini Tasks'''
#1 finding the maximun and minimum number of list using min and max method
number=[1,2,3,4,5,6,7,8,9,10]
max_num=max(number)
print(max_num)

#2 minimum number
min_num=min(number)
print(min_num)

#3 sum
sum=sum(number)
print(sum)

#4 checking if all elements in lsit is true using all()
true=all(number)
print(true)


#5 checking if all elements in lsit is true using any()
any=any(number)
print(any)

#6 length of list uing len()
length=len(number)
print(length)

#7 converting string into character using list()
Apple=('apple')
new_apple=list(Apple)
print(new_apple)

#8 



#9 
new=list(range(6))
print(new)