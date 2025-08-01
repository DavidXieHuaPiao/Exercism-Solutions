from math import sqrt
def score(x, y):
    magn=sqrt(x**2+y**2)
    if magn>10:
        return 0
    if magn>5:
        return 1
    if magn>1:
        return 5
    return 10