def is_armstrong_number(number):
    nn = str(number)
    check = 0
    for i in nn:
        check += int(i)**len(nn)
    return int(nn) == check