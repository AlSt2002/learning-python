def is_valid_triangle(sides):
    if (sides[0] == 0 and sides[1] == 0 and sides[2] == 0):
        return False
    if ((sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])):
        return True
    return False
    



def equilateral(sides):
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]
    pass


def isosceles(sides):
    return is_valid_triangle(sides) and (
        sides[0] == sides[1]
        or sides[0] == sides[2]
        or sides[1] == sides[2]
    )
    pass


def scalene(sides):
    return is_valid_triangle(sides) and (
        sides[0] != sides[1]
        and sides[0] != sides[2]
        and sides[1] != sides[2]
    )
    pass
