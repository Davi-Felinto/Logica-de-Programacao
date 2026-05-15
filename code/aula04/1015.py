from math import sqrt

x1, y1 = map(float, input(). split())
x2, y2 = map(float, input(). split())

print(f'{(sqrt((x1 - x2)**2 + (y2 - y1)**2)):.4f}')