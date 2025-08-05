def is_valid(isbn):
    new_isbn = str(isbn).replace("-", "")
    count = 0
    start = 10
    if len(new_isbn)==10 and (new_isbn[-1] == "X" or new_isbn[-1] in "1234567890"):
        for i in new_isbn:
            if i != "X" and i in "1234567890":
                count+= int(i)*start
                start-=1
            else:
                count+=10
    else:
            return False

    return count%11 == 0

