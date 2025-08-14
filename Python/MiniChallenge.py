
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
state=state.replace("a","*")
state=state.replace("e","*")
state=state.replace("i","*")
state=state.replace("o","*")
state=state.replace("u","*")
print(state)

#username generator
user1=input("First Name:")
user2=input("Last Name:")
user3=input("Birth year:")

print()