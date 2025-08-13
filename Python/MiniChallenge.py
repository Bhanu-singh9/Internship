
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
vowels = "aeiouAEIOU"
for i in vowels:
    state=state.replace(i,"*")
print(state)