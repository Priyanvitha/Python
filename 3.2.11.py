#3.2.11   LAB   The continue statement – the Pretty Vowel Eater
user_word = input("Enter the word : ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU" :
        continue
    word_without_vowels += letter
print(word_without_vowels)