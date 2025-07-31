def response(hey_bob):
    hey_bob=hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
            
    if hey_bob.endswith("?") and hey_bob.isupper() == True:
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure."
    if hey_bob.isupper() == True:
        return "Whoa, chill out!"
    return "Whatever."