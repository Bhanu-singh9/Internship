
# #Mini Challenges
text=input("Insert a text:")
print(text[::-1])


if text == text[::-1]:
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")

# Count the number of vowels in a sentence
state=input("Insert a sentence:")
words=state.split()
print(words)
print(len(words))
a=state.replace("a","*")
b=a.replace("e","*")
c=b.replace("i","*")
d=c.replace("o","*")
e=d.replace("u","*")

print(e)

