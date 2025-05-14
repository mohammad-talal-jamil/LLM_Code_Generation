def encode(message):
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        else:
            index = vowels.find(char)
            if index != -1:
                encoded += vowels[(index + 2) % 5]
            else:
                encoded += char
    return encoded
