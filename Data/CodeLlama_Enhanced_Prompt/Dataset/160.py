def do_algebra(operator, operand):
    return eval(' '.join(str(op) for op in operator) + ' '.join(str(op) for op in operand))
