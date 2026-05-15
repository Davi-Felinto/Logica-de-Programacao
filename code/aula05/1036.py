from math import sqrt
A, B, C = map(float, input().split())

dis = (B**2 - 4*A*C)

if dis >= 0 and A != 0:
    R1=(-B + sqrt(dis))/(2*A)
    R2=(-B - sqrt(dis))/(2*A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print('Impossivel alcular')