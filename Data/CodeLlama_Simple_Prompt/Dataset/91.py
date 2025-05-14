def is_bored(S):
    return len([word for word in S.split() if word.startswith("I")])
