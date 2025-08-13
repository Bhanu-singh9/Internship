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
