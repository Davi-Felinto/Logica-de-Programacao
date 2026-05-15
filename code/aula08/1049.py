# leitura das entradas
grupo = input().strip()
classi = input().strip()
ali = input().strip()

# estrutura de calssificação
# caso o grupo seja vertebrado
if grupo == "vertebrado": 
    # caso classificação seja ave
    if classi == "ave":
        if ali == "carnivoro":# caso alimentação seja carnivoro
            print("aguia")
        elif ali == "onivoro":# caso alimentação seja onivoro
            print('pomba')
# caso classificação seja mamifero
    elif classi == "mamifero":
        if ali == "herbivoro":# caso alimentação seja herbivoro
            print("vaca")
        elif ali == "onivoro": # caso alimentação seja onivoro
            print('homem')

# caso o grupo seja invertebrado
elif grupo == "invertebrado":
    # caso classificação seja inseto
    if classi == "inseto":
        if ali == "hematofago": # caso alimentação seja hematofago
            print("pulga")
        elif ali == "herbivoro": # caso alimentação seja herbivoro
            print("lagarta")
    # caso classificação seja anelideo
    elif classi == "anelideo":
        if ali == "hematofago": # caso alimentação seja hematofago
            print("sanguessuga")
        elif ali == "onivoro": # caso alimentação seja onivoro
            print("minhoca")