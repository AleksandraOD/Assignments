class Roman:
    def __init__(self, number):
        if type(number) != int:
            raise ValueError
        elif number < 1 or number > 1999:
            raise ValueError
        self.number = number
        self.numbers = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                        100: 'C', 500: 'D', 1000: 'M'}
        self.picture = ''
        k = 0
        while number > 0:
            numeral = number % 10
            number = number // 10
            if numeral < 4:
                self.picture = self.numbers[10 ** k] * numeral + self.picture
            if numeral == 4:
                self.picture = (self.numbers[10 ** k]
                                + self.numbers[5 * 10 ** k] + self.picture)
            if 4 < numeral < 9:
                self.picture = (self.numbers[5 * 10 ** k]
                                + self.numbers[10 ** k] * (numeral % 5)
                                + self.picture)
            if numeral == 9:
                self.picture = (self.numbers[10 ** k]
                                + self.numbers[10 ** (k + 1)] + self.picture)
            k += 1

    def __str__(self):
        return self.picture

    def __int__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __add__(self, other):
        if self.number + other.number > 1999:
            raise ValueError('число дожно быть > (-1) и < 2000')
        else:
            return self.number + other.number
