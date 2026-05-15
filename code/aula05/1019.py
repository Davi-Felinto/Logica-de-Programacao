N = int(input()) # entrada de segundos

hr = (N//3600) #divisão inteira para descobrir a hr
seg = (N%3600) #resto da entrada asicionado a seg
min = (seg//60) #divisão inteira para descobrir os min
seg = (seg%60) #resto dos min para descobrir os seg

print(f"{hr}:{min}:{seg}") 