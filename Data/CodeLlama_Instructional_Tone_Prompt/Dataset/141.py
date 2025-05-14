def file_name_check(file_name):
    if len(file_name) > 3:
        return 'No'
    if not file_name.startswith(('a', 'b', 'c')):
        return 'No'
    if not file_name.endswith(('.txt', '.exe', '.dll')):
        return 'No'
    return 'Yes'
