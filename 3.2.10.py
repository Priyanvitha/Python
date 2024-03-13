#3.2.10 The continue statement – the Ugly Vowel Eater
user_word = input("Enter the word : ")# Prompt the user to enter a word
user_word = user_word.upper() # and assign it to the user_word variable.

for letter in user_word:
    if letter in "AEIOU":
     continue
    print(letter)

