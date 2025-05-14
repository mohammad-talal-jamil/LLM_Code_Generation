def remove_vowels(text):
    vowels = 'aeiou'
    return ''.join([char for char in text if char.lower() not in vowels])
