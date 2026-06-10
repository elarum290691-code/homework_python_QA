import math


def square(side):
    area = side * side
    if not area.is_integer():
        area = math.ceil(area)
    return area


side_length = 5.7
area_result = square(side_length)

print(f'Площадь квадрата со стороной {side_length} = {area_result}')
