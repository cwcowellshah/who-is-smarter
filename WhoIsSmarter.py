# Figure out how many letters (on average) there are per word

# take all the text
brown_1_file = open('brown_1.txt')
brown_1_text = brown_1_file.read()
brown_1_file.close()

# replace carriage returns with spaces
brown_1_text = brown_1_text.replace('\n', ' ')

# chop the text into words, one line at a time
words_in_speech = brown_1_text.split()

# count how many characters are in the words
num_chars_in_speech = 0
for word in words_in_speech:
    num_chars_in_speech += len(word)

# find the mean of the number of characters in words
num_words_in_speech = len(words_in_speech)
mean_letters_per_word = num_chars_in_speech / num_words_in_speech

print(mean_letters_per_word)