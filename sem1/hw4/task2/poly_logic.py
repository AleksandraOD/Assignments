def derivative(poly):
    if poly == '0':
        return poly
    if poly == '1':
        return '0'
    poly = poly.replace(' ', '').replace('^', '')
    if poly[:1] == '-':
        first_sign = True
    else:
        first_sign = False
    result = ''
    coeff = ''
    deg = ''
    signs = []
    terms = []
    d = False
    for sign in poly[:-1]:
        if d:
            if sign.isdigit():
                deg += sign
            else:
                signs.append(sign)
                terms.append(term_creation(coeff, deg))
                d = False
                coeff = ''
                deg = ''
        else:
            if sign.isdigit():
                coeff += sign
            elif sign == '-' or sign == '+':
                signs.append(sign)
            else:
                d = True
    if d:
        deg += poly[-1:]
        terms.append(term_creation(coeff, deg))
    if first_sign:
        for i in range(len(terms)):
            result += + signs[i] + terms[i]
    else:
        for i in range(len(terms)):
            result += terms[i] + signs[i]
        result = result[:-1]
    return result


def term_creation(coeff, deg):
    if deg == '':
        if coeff == '':
            return '1'
        else:
            return coeff
    else:
        if coeff == '':
            coeff = deg
            deg = str(int(deg) - 1)
            if deg == '1':
                return coeff + 'x'
            else:
                return coeff + 'x^' + deg
        else:
            coeff = str(int(coeff) * int(deg))
            deg = str(int(deg) - 1)
            if deg == '1':
                return coeff + 'x'
            else:
                return coeff + 'x^' + deg
