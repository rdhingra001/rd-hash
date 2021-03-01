import random
import nltk
import base64

def _bag_of_chars(word):
    bag = []

    for char in word:
        bag.append(char)
    
    return bag

def encrypt(input):
    # Put all of the words inputted into a list
    words_bag = input.split()

    # Iterate through all of the words in the bag and convert them all into base64
    word_char_bag = []
    base64_word_bag = []
    for word in words_bag:
        char_bag = _bag_of_chars(word)
        word_char_bag.append(char_bag)
        base64_char_bag = []
        for char in char_bag:
            char_base64 = base64.b64encode(bytes(char, 'utf-8'))
            base64_char_bag.append(char_base64)
        base64_word_bag.append(base64_char_bag)
    
    # Clean the base64-encoded characters
    for chars in base64_word_bag:
        for base64char in chars:
            base64_char_bag = []
            base64char = str(base64char)
            base64char_cleaned = base64char.replace("==", "", 2)
            base64char_cleaned = base64char_cleaned.replace('b', '')
            base64_char_bag.append(base64char_cleaned)
        print(base64_char_bag)


    

def decrypt(input):
    pass

encrypt('ronit')