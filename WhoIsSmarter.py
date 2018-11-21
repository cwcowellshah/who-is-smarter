def calculate_mean_letters_per_word(text_file_name):
    # read the text from a file
    text_file = open(text_file_name)
    text = text_file.read()
    text_file.close()

    # replace punctuation with empty strings
    punctuation_marks = ['.', ',', ':', ';', '(', ')', '!', '?', '[', ']',
                         '$', '"', "'", '-', '●' '\t', '“', '”']
    for punctuation_mark in punctuation_marks:
        text = text.replace(punctuation_mark, '')

    # chop the text into words, using spaces as word dividers
    words_in_text = text.split()

    # count how many characters are in the ALL the words of the speech
    num_chars_in_text = 0
    for word in words_in_text:
        num_chars_in_text += len(word)

    # find the mean letters per word
    num_words_in_text = len(words_in_text)
    mean_letters_per_word = num_chars_in_text / num_words_in_text

    return mean_letters_per_word


def calculate_num_words(text_file_name):
    # read the text from a file
    text_file = open(text_file_name)
    text = text_file.read()
    text_file.close()

    # chop the text into words, using spaces as word dividers
    words_in_text = text.split()
    num_words_in_text = len(words_in_text)

    return num_words_in_text


def calculate_uncommon_words_percent(text_file_name):
    # read the text from a file
    text_file = open(text_file_name)
    text = text_file.read()
    text_file.close()

    # replace punctuation with empty strings
    punctuation_marks = ['.', ',', ':', ';', '(', ')', '!', '?', '[', ']',
                         '$', '"', "'", '-', '●' '\t', '“', '”']
    for punctuation_mark in punctuation_marks:
        text = text.replace(punctuation_mark, '')

    # chop the text into words, using spaces as word dividers
    words_in_text = text.split()

    # read the 1000 most common English words from a file
    common_words_file = open('most_common_words.txt')
    common_words_text = common_words_file.read()
    common_words_file.close()

    common_words = common_words_text.split()

    for each_word in words_in_text:
        print(each_word + ': ' + str((each_word in common_words)))


print('Mean letters per word')
print('Fake:', calculate_mean_letters_per_word('Fake.txt'))
print('Brown:', calculate_mean_letters_per_word('Brown.txt'))
print('Ishiguro:', calculate_mean_letters_per_word('Ishiguro.txt'))
print('Clinton:', calculate_mean_letters_per_word('Clinton.txt'))
print('Trump:', calculate_mean_letters_per_word('Trump.txt'))

print('----')
print('Length of text')
print('Fake:', calculate_num_words('Fake.txt'))
print('Brown:', calculate_num_words('Brown.txt'))
print('Ishiguro:', calculate_num_words('Ishiguro.txt'))
print('Clinton:', calculate_num_words('Clinton.txt'))
print('Trump:', calculate_num_words('Trump.txt'))

calculate_uncommon_words_percent('Brown.txt')