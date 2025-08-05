def rebase(input_base, digits, output_base):
    if not input_base>=2:
        raise ValueError("input base must be >= 2")
    for i in digits:
        if not 0<=i<input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if not output_base>=2:
        raise ValueError("output base must be >= 2")

    number=0
    count=len(digits)-1
    final=[]
    for i in digits:
        number+=i*(input_base**count)
        count-=1

    while number//output_base!=0:
        final.append(number%output_base)
        number//=output_base
    final.append(number%output_base)

    return list(reversed(final))