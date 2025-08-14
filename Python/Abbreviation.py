#Abbreviation
text=input  ("Write a text:")
words=text.split()
c=""
for i in words:
    c+=i[0]
print("Abbreviation:", c.upper())


#Replacing words
sentence=input("Enter a sentence:")
print(sentence)
old_word=input("Enter a old word you want to replace:")
new_word=input("Enter a new word:")

new_sentence=sentence.replace(old_word,new_word)
print("Replaced Sentence:",new_sentence)

'''User name generator
'''
user1=input("First Name:")
user2=input("Last Name:")
user3=input("birthyear:")
print(user1+user2+user3)


#password generator (asked for user input resversed it using negative indexing and added random number)
password=input("Enter a password:")
print(password)
print(password[::-1]+"98")

#pig latin converter
pig=("python")
print(pig)

