def vowels_count(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    if word.endswith("y"):
        count -= 1
    return count
