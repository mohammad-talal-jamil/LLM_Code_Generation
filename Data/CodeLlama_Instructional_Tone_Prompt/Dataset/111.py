def histogram(string):
    # Create a dictionary to store the counts of each letter
    letter_counts = {}
    for char in string:
        if char not in letter_counts:
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1

    # Find the letter with the highest count
    highest_count = 0
    for letter, count in letter_counts.items():
        if count > highest_count:
            highest_count = count

    # Create a dictionary to store the letters with the highest count
    highest_count_letters = {}
    for letter, count in letter_counts.items():
        if count == highest_count:
            highest_count_letters[letter] = count

    return highest_count_letters
