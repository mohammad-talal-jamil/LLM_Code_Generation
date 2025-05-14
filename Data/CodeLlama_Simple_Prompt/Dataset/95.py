def check_dict_case(my_dict):
    if not my_dict:
        return False
    first_key = list(my_dict.keys())[0]
    return all(key.islower() or key.isupper() for key in my_dict.keys())
