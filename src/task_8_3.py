"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε ."""

import math

N = int(input("vvedite N: "))


def Sin1(x, N):
    s = 0
    for i in range(1, N + 1):
        s += (-1) ** i * x ** (2 * i + 1) / math.factorial((2 * i + 1))
    return math.sin(s)


y = Sin1(2, N)
print(y)
