# # Ceasar cipher pentru un cuvant

# while True:
#     try:
#         cuv = input('Introduceti cuvantul care urmeaza sa fie criptat: ')

#         cheie = int(input('Introduceti un numar intreg, care va fi cheia cifrului: '))

#         break

#     except:
#         print('Date de intrare invalide!')

# # transformam toate literele cuvantului in majuscule
# cuv = cuv.upper()

# l = len(cuv) # memoram lungimea cuvantului intr-o  variabila
# cuv2 = ''

# for i in range(l):
#     cod = 65 + (ord(cuv[i]) - 65 + cheie) % 26
#     cuv2 += chr(cod)

# print(cuv2)
    
# Caesar cipher pentru o fraza

# introducerea de catre utilizator a datelor de intrare
while True:
    try:
        fraza = input('Introduceti o fraza care urmeaza sa fie criptata: ')

        cheie = int(input('Introduceti un numar intreg, care va fi cheia cifrului: '))

        break

    except:
        print('Date de intrare invalide!')

def cifru_caesar(fraza, cheie = 0):
    # verificam daca argumetii sunt valizi
    if type(fraza) != str or type(cheie) != int:
        print('Date de intrare invalide!')
        return None

    l = len(fraza)
    fraza_finala = ''

    for i in range(l):
        if ord(fraza[i]) >= 65 and ord(fraza[i]) <= 90:
            cod = 65 + (ord(fraza[i]) - 65 + cheie) % 26
            fraza_finala += chr(cod)
        elif ord(fraza[i]) >= 97 and ord(fraza[i]) <= 122:
            cod = 97 + (ord(fraza[i]) - 97 + cheie) % 26
            fraza_finala += chr(cod)
        else:
            fraza_finala += fraza[i]

    del l, i, cod

    return fraza_finala

criptare = cifru_caesar(fraza,cheie)

print(criptare)