def square(number):
    if number in range(1,65):
        a = 2**(number-1)
        return a
    else:
        raise ValueError("square must be between 1 and 64")

    


def total():
    q = 0
    for i in range (1, 65):
        q += 2**(i-1)
    return q
