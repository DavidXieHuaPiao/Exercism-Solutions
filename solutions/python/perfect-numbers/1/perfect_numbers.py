def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) != int or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        aliquot_sum = 0
        for i in range(1, number):
            if number%i==0:
                aliquot_sum+=i
        if number<aliquot_sum:
            return "abundant"
        if number>aliquot_sum:
            return "deficient"
        return "perfect"
