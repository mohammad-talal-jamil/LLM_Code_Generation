def strongest_extension(class_name, extensions):
    return class_name + '.' + max(extensions, key=lambda x: len([c for c in x if c.isupper()]) - len([c for c in x if c.islower()]))
