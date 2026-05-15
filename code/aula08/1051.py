sal = float(input())

per = 0
imposto = 0

if sal > 2000:
    per = 0.08
elif sal > 3000:
    per = 0.18 
elif sal > 4500:
    per = 0.28

if per == 0.08:
    imposto = (sal - 2000) * 00.8
if per == 0.18:
    imposto = ((sal - 3000) * 0.18) + (1000 * 0.08) 

print ([imposto])