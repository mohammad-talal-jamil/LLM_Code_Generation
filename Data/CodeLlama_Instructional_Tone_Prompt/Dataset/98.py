def count_upper(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i, c in enumerate(s):
        if c in vowels and i % 2 == 0:
            count += 1
    return count
