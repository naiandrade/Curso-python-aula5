# leia uma palavra e verifique se ela contem vogais
letra_a=0
letra_e=0
letra_i=0
letra_o=0
letra_u=0
palavra = input("digite uma palavra")
for letra in palavra:
    if letra == "a":
        letra_a +=1
    elif letra == "e":
        letra_a +=1
    elif letra == "i":
        letra_a +=1
    elif letra == "o":
        letra_a +=1
    elif letra == "u":
        letra_a +=1

print(letra_a, letra_e, letra_i, letra_o, letra_u)