def steps(number):
    if type(number) == int and number > 0:
        count = 0
        while True:
            if number == 1:
                return count
            elif number%2 == 0:
                number/=2
            else:
                number = number*3 + 1
            count += 1
    else:
        raise ValueError("Only positive integers are allowed")
