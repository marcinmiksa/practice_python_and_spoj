# ROWNANIE - Równanie kwadratowe
# Napisz program, który wyznacza liczbę pierwiastków rzeczywistych równania kwadratowego.
# https://pl.spoj.com/problems/ROWNANIE/

A, B, C = map(float, input().split())

delta = B * B - 4 * A * C

if delta > 0:
    print('2')
elif delta == 0:
    print('1')
else:
    print('0')
