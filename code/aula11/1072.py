N = int(input())

in_ = 0
out = 0

for i in range(N):
    x = int(input())
    if 10 <= x <= 20:
        in_ += 1
    else:
        out += 1

print(f'{in_} in')
print(f'{out} out') 