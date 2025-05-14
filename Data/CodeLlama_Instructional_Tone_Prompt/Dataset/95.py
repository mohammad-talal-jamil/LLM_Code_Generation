def check_dict_case(my_dict):
    if not my_dict:
        return False
    first_key = list(my_dict.keys())[0]
    if first_key.islower():
        for key in my_dict.keys():
            if not key.islower():
                return False
    elif first_key.isupper():
        for key in my_dict.keys():
            if not key.isupper():
                return False
    else:
        return False
    return True
