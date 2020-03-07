
# The "words.txt" file contains a single line of 1000 words, separated by commas.


# This function turns a single-line-file, with words separated by commas, into a list-object.
# Optional parameter: word_amount --> choose the amount of words you want in the list ("words.txt" contains 1000 words)
def create_word_list(filename, word_amount=None):
    with open(str(filename), 'r') as reference:
        words = reference.readline()
        word_list = words.split()

        for idx, word in enumerate(word_list):  # removes commas
            word_list[idx] = word.strip(',')

    reference.close()

    if word_amount:
        word_list = word_list[:word_amount]
    return word_list


# This function creates a new file where all the words are on it's own line (trailing newline at
# the end)
def create_word_file(filename, word_list):
    with open(str(filename), 'w+') as new_file:
        for word in word_list:
            new_file.write(f'{word.strip(",")}\n')
    new_file.close()


if __name__ == '__main__':
    read_file = 'words.txt'
    write_file = 'words_list.txt'
    word_list = create_word_list(read_file)
    create_word_file(write_file, word_list)
