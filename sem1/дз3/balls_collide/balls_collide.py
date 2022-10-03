def balls_collide(coordinates_one, coordinates_two):
    x1, y1, r1 = (coordinates_one)
    x2, y2, r2 = (coordinates_two)
    if r1 < 0 or r2 < 0:
        raise ValueError("Отрицательное число")
    a = x1 - x2
    b = y1 - y2
    distance = (a) ** 2 + (b) ** 2
    if distance <= (r1 + r2) ** 2:
        return True
    else:
        return False
