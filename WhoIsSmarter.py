def calculate_mean_letters_per_word(text_file_name):
    # read the text from a file
    fake_speech_file = open(text_file_name)
    fake_speech_text = fake_speech_file.read()
    fake_speech_file.close()

    # replace carriage returns with spaces
    fake_speech_text = fake_speech_text.replace('\n', ' ')

    # replace punctuation with empty strings
    punctuation_marks = ['.', ',', ':', ';', '(', ')', '!', '?', '[', ']', '$', '"', "'", '\t']
    for punctuation_mark in punctuation_marks:
        fake_speech_text = fake_speech_text.replace(punctuation_mark, '')

    # chop the text into words, using spaces as word dividers
    words_in_fake_speech = fake_speech_text.split()

    # count how many characters are in the ALL the words of the speech
    num_chars_in_fake_speech = 0
    for word in words_in_fake_speech:
        num_chars_in_fake_speech += len(word)

    # find the mean letters per word
    num_words_in_fake_speech = len(words_in_fake_speech)
    mean_letters_per_word = num_chars_in_fake_speech / num_words_in_fake_speech

    return mean_letters_per_word

# ----


print(calculate_mean_letters_per_word('fake_speech.txt'))
print(calculate_mean_letters_per_word('brown_1.txt'))
