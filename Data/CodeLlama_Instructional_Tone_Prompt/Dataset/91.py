def is_bored(S):
    count = 0
    for sentence in S.split(".") + S.split("?") + S.split("!"):
        if sentence.startswith("I"):
            count += 1
    return count
