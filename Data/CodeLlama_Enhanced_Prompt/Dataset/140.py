def fix_spaces(text):
    new_text = ""
    space_count = 0
    for char in text:
        if char == " ":
            space_count += 1
            if space_count == 1:
                new_text += "_"
            elif space_count > 2:
                new_text += "-"
        else:
            space_count = 0
            new_text += char
    if space_count > 2:
        new_text += "-"
    return new_text
