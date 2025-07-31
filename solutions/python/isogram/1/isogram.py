def is_isogram(string):
    comp = string.lower()
    for i in comp:
        splitted = comp.split(i)
        if len(splitted) != 2 and i != " " and i != "-":
            return False
    return True
