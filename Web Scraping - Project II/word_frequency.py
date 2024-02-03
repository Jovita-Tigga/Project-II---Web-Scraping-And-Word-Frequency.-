# Import Libraries
import string

def strip_punctuations(line):
     for character in string.punctuation:
        line = line.replace(character, "")
     return line

# Upload the filepath
filepath = "C:\\Users\\Jovita\\NextHikes_Projects\\Web Scraping - Project II\\Data.txt"

# Establish an int dictionary word count = {}
word_count = {}

with open(filepath,'r') as fi:
# For each line in the file
     for line in fi:
# Remove the punctuation 
        line = strip_punctuations(line)
# Sperate the words by spaces into a list
        words = line.split()

# For each word in words
        for word in words:
# Convert the word into lowercase
            word = word.lower()
# Check if it NOT in out dictionary
            if word not in word_count:
# If not create a new entry for it
                word_count[word] = 0
# Then increment its count by 1
            word_count[word] += 1
# List 10 of the keys in no particular order
list(word_count.keys())[:10]

# Traverse ten words and print their count
ten_words = list(word_count.keys())[:10]
for word in ten_words:
# Word must take up a minimal of 15 spaces; count can take minimum of 8
    print("{0:15}{1:8d}".format(word, word_count[word]))


    

    
    






