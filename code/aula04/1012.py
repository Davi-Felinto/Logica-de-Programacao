A, B, C = map(float, input().split())
pi = 3.141559

Area_tri = (A*C)/2
Area_cir = (pi* C**2)
Area_trape = ((A + B)*C)/2
Area_qua = (B**2)
Area_retan = (A*B)

print(f"TRIANGULO: {Area_tri:.3f}")
print(f"CIRCULO: {Area_cir:.3f}")
print(f"TRAPEZIO: {Area_trape:.3f}")
print(f"QUADRADO: {Area_qua:.3f}")
print(f"RETANGULO: {Area_retan:.3f}")