import math

class Fraction:
    instances = {}  # Словарь для хранения экземпляров

    def __new__(cls, *args):
        if len(args) == 2:
            num, den = args[0], args[1]
        elif '/' in args[0]:
            num, den = map(int, args[0].split('/'))
        else:
            raise ValueError("Invalid arguments")

        # Упрощаем дробь при создании
        gcd = math.gcd(num, den)
        num //= gcd
        den //= gcd
        if den < 0:  # Приводим к стандартному виду
            num *= -1
            den *= -1

        # Создаем уникальный ключ для хранения экземпляров
        key = (num, den)
        if key not in cls.instances:
            instance = super().__new__(cls)
            instance.num = num
            instance.den = den
            cls.instances[key] = instance
        return cls.instances[key]

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f"Fraction('{self.num}/{self.den}')"

    def neg(self):
        return Fraction(-self.num, self.den)

    def add(self, other):
        num = (self.num * other.den + other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def sub(self, other):
        num = (self.num * other.den - other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def __iadd__(self, other):
        result = self.add(other)
        self.num, self.den = result.num, result.den
        return self

    def __isub__(self, other):
        result = self.sub(other)
        self.num, self.den = result.num, result.den
        return self
a = {'zlocty' : 'suka'}
