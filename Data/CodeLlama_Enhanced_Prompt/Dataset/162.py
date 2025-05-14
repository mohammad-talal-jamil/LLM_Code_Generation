def string_to_md5(text):
    if not text:
        return None
    from hashlib import md5
    return md5(text.encode()).hexdigest()
