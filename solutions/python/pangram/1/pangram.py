def is_pangram(sentence):
    comp = sentence.lower().replace(" ", "")
    for i in "qwertyuiopasdfghjklzxcvbnm":
        if i not in comp:
            return False
    return bool(comp)
