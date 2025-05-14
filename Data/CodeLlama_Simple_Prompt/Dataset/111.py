def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # split the test string into a list of individual letters
    letters = test.split()
    # create an empty dictionary to store the counts
    counts = {}
    # loop through the list of letters
    for letter in letters:
        # if the letter is already in the dictionary, increment its count
        if letter in counts:
            counts[letter] += 1
        # otherwise, add the letter to the dictionary and set its count to 1
        else:
            counts[letter] = 1
    # find the letter with the highest count
    highest_count = max(counts.values())
    # create a list of all letters with the highest count
    highest_count_letters = [letter for letter,
                             count in counts.items() if count == highest_count]
    # return the dictionary with the letters and their corresponding counts
    return {letter: counts[letter] for letter in highest_count_letters}
