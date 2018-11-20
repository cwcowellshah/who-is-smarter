# Figure out how many letters (on average) there are per word

# read all the text from a file
fake_speech_file = open('fake_speech_file.txt')
fake_speech_text = fake_speech_file.read()
fake_speech_file.close()

# replace carriage returns with spaces
brown_1_text = brown_1_text.replace('\n', ' ')

# replace punctuation with empty strings


# chop the text into words, by cutting it every time there's a space
words_in_speech = brown_1_text.split()

# count how many characters are in the words
num_chars_in_speech = 0
for word in words_in_speech:
    num_chars_in_speech += len(word)

# find the mean of the number of characters in words
num_words_in_speech = len(words_in_speech)
mean_letters_per_word = num_chars_in_speech / num_words_in_speech

print(mean_letters_per_word)