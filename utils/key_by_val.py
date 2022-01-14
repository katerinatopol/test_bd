def key_by_val(dictionary, val):
    for k, v in dictionary.items():
        if val in v:
            return k
