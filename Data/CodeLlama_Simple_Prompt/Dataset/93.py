def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        elif char in vowels:
            index = vowels.index(char)
            new_index = (index + 2) % 5
            result += vowels[new_index]
        else:
            result += char
    return result
