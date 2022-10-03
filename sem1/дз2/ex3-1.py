def pascal_triangle(n):
    if n <= 0:
        raise ValueError
    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    row = [1, 1]
    for i in range(2, n):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

for row in pascal_triangle(3):
    print(row)
