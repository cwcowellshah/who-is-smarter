from nltk.stem import LancasterStemmer


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
                         '$', '"', "'", '’', '-', '–', '●', '\t', '“', '”', '\n',
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for punctuation_mark in punctuation_marks:
        text = text.replace(punctuation_mark, ' ')

    # chop the text into words, using spaces as word dividers
    words_in_text = text.split()

    stemmer = LancasterStemmer()
    stems_in_text = []
    for word in words_in_text:
        stem = stemmer.stem(word)
        lower_case_stem = stem.lower()
        stems_in_text.append(lower_case_stem)

    # read the 1000 most common English words from a file
    common_words_file = open('most_common_words.txt')
    common_words_text = common_words_file.read()
    common_words_file.close()

    common_words = common_words_text.split()

    common_stems = []
    for word in common_words:
        stem = stemmer.stem(word)
        lower_case_stem = stem.lower()
        common_stems.append(lower_case_stem)

    uncommon_stems = []
    for stem in stems_in_text:
        if not (stem in common_stems):
            uncommon_stems.append(stem)

    pct_uncommon_stems = len(uncommon_stems) / len(stems_in_text)
    rounded_pct_uncommon_stems = round(pct_uncommon_stems, 3)
    return rounded_pct_uncommon_stems



people = ['Brown', 'Clinton', 'Ishiguro', 'Trump', 'Fake']
for person in people:
    file_name = person + '.txt'
    print(person)
    print('\t' + str(calculate_mean_letters_per_word(file_name)) + ' mean letters per word')
    print('\t' + str(calculate_num_words(file_name)) + ' words')
    print('\t' + str(calculate_uncommon_words_percent(file_name) * 100) + ' percent uncommon words')
