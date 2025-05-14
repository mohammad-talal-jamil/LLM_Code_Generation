def is_bored(S):
    return sum(1 for i in S.split('.') if i.startswith('I '))
