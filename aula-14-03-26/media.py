nota1 = float (input ("nota1="))
nota2 = float (input ("nota2="))
nota3 = float (input ("nota3="))
media = (nota1+nota2+nota3)/3
print("a media é:", media)
if media >0 and media <5:
    print("reprovado")
elif media >=5 and media<=6.9:
    print ("recuperação")
elif media >=6.9 and media<10:
    print ("aprovado")    
 else:    
    print ("você foi aprovado")    
