def is_valid_triangle(sides):
    if len(sides) != 3:
        raise ValueError("A triangle must have exactly three sides.")
    for i in sides:
        if i <= 0:
            return False
    a, b, c = sorted(sides)

    if a + b < c:
        return False

    return True

def equilateral(sides):
    return sides[0]==sides[1]==sides[2] and is_valid_triangle(sides)
        


def isosceles(sides):
    return (sides[0]==sides[1] or sides[1]==sides[2] or sides[2]==sides[0]) and is_valid_triangle(sides)


def scalene(sides):
    return (sides[0]!=sides[1] and sides[1]!=sides[2] and sides[2]!= sides[0]) and is_valid_triangle (sides)
