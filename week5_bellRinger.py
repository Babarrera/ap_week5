# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character. 
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char =print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index=print(magic.index('r'))
last_a_index=print(magic.rindex('a'))
# rindex finds the last occurrence of a specified value.
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# hij=print(alphabet[7:10])
hij=print(alphabet.index('hij'))
hiji=print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
m_index= print(alphabet.index('m'))
every_second= print(alphabet[0:13:2])

#  c. Reverse the entire string using slicing.
reversed_alphabet=print(alphabet[ : :-1])

i_have_a_dream= "i have a dream that one day this nation will rise up" 
reversed_i_have_a_dream=print(i_have_a_dream[ : :-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.