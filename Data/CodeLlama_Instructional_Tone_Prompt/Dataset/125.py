def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.split(",")
    else:
        return len([c for c in txt if c.islower() and ord(c) % 2 == 1])
