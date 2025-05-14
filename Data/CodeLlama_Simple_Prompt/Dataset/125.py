def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.split(",")
    else:
        result = 0
        for char in txt:
            if char.islower():
                result += 1
        return result
