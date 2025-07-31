def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for i in text:
        if i in plain:
            cipher+=plain[plain.index(i)+key-26]
        elif i.lower() in plain:
            cipher+=plain[plain.index(i.lower())+key-26].upper()
        else:
            cipher+=i

    return cipher