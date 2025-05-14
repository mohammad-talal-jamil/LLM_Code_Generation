def anti_shuffle(s):
    words = s.split()
    return ' '.join(sorted(words, key=lambda x: sorted(x)))
