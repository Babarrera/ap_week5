# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.

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

# ===============================================
# Problem Sets on String Indexing, Slicing & Methods
# ===============================================

# -------------------------------
#  Problem Set 1: Indexing and Slicing Strings
# -------------------------------

# Basic Indexing
magic = 'abracadabra'

# a. Retrieve the 5th character (index 4 because counting starts from 0)
fifth_char = magic[4]

# b. Retrieve the second to last character (index -2 means 2nd from end)
second_last_char = magic[-2]

# c. Find the first occurrence of the letter 'c'
first_c = magic.index('c')


# Advanced Slicing
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a. Extract the letters 'hij' (start at index 7, stop before 10)
hij = alphabet[7:10]

# b. Extract every second letter from 'a' to 'm'
# start=0, stop=13 (m is index 12), step=2
every_second_to_m = alphabet[0:13:2]

# c. Reverse the entire string using slicing
# [::-1] means step backwards by 1
reverse_alpha = alphabet[::-1]


# -------------------------------
#  Problem Set 2: Extracting Information
# -------------------------------

# From Descriptions
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Split at the dash "-" and take the last part, remove extra spaces
name = quote.split('-')[-1].strip()


# Manipulating Words
info = "Python is fun. Fun is good. Good is subjective."

# a. Extract the word 'subjective' without knowing its position
# Split into words, take last word, strip the period at the end
subjective = info.split()[-1].strip('.')

# b. Extract every third word
# [::3] means take every 3rd word starting from index 0
every_third_word = info.split()[::3]

# c. Reverse the positions of the words but keep letters inside each word same
# Split → reverse list → join back to string
reversed_words = ' '.join(info.split()[::-1])


# -------------------------------
#  Problem Set 3: String Methods
# -------------------------------

# Upper & Lower
text = "MAY THE FORCE BE WITH YOU."

# Convert entire string to lowercase
lower_text = text.lower()

# String Joining and Splitting
motto = ["Make", "haste", "slowly."]

# a. Join list items into one string with spaces
motto_string = ' '.join(motto)

# b. Split the string at every letter 'a'
split_at_a = motto_string.split('a')

# Replacing Words
sentence = "Life is what happens when you are busy making other plans."

# a. Replace "busy" with "distracted"
replace_busy = sentence.replace("busy", "distracted")

# b. Replace "plans" with "mistakes"
replace_plans = replace_busy.replace("plans", "mistakes")


# -------------------------------
#  Problem Set 4: String Properties and Advanced Operations
# -------------------------------

# Repetition
word = "Iteration"
# Repeat the word 7 times
repeated = word * 7

# Word Search
quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
# Check if the word "moonlight" is present in the quote
has_moonlight = "moonlight" in quote2

# Length and Count
phrase = "Supercalifragilisticexpialidocious"

# a. Count total characters
length = len(phrase)

# b. Count how many times 'i' appears
count_i = phrase.count('i')


# -------------------------------
# 🧾 Print All Results
# -------------------------------
print("=== Problem Set 1 ===")
print("5th character:", fifth_char)
print("Second to last character:", second_last_char)
print("First occurrence of 'c':", first_c)
print("Letters 'hij':", hij)
print("Every 2nd letter from a–m:", every_second_to_m)
print("Reversed alphabet:", reverse_alpha)
print()

print("=== Problem Set 2 ===")
print("Famous personality:", name)
print("Extracted word:", subjective)
print("Every 3rd word:", every_third_word)
print("Reversed word order:", reversed_words)
print()

print("=== Problem Set 3 ===")
print("Lowercase text:", lower_text)
print("Joined motto:", motto_string)
print("Split at 'a':", split_at_a)
print("Modified sentence:", replace_plans)
print()

print("=== Problem Set 4 ===")
print("Word repeated 7 times:", repeated)
print("Contains 'moonlight'?", has_moonlight)
print("Length of word:", length)
print("Count of 'i':", count_i)
