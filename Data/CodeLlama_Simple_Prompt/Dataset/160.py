def do_algebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
        result = eval(str(result) + operator[i] + str(operand[i+1]))
    return result
