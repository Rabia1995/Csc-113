def letter_in_list(word):
    find_value = 97
    letters = []
    while find_value <= 122:
        letters.append(chr(find_value))
        find_value = find_value + 1
    return letters


def find_frequent_letters(word):
    find_value = 97
    letter_size = []
    while find_value <= 122:
        letter_size.append((word.count(chr(find_value))))
        find_value = find_value + 1
    return letter_size


def probability(words):

    probabilities = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                     'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                     'y': 0, 'z': 0}

    # go though letter in the file and count freq
    read_words = words.readlines()
    read_string = ''.join(read_words)
    read_string.lower()
    frequencies = dict(zip(letter_in_list(read_string), find_frequent_letters(read_string)))
    print(frequencies)

    # adds up all the frequencies
    total_freq = 0
    for letter in frequencies:
        total_freq = total_freq + frequencies[letter]

    # calculate the probabilities of each letter
    for letter in probabilities:
        probabilities[letter] = frequencies[letter] / total_freq

    # return a list of sorted tuples for each letter by frequency
    return sorted(list(probabilities.items()), key=lambda x: x[1], reverse=True)


