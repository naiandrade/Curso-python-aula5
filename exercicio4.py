#Resolva - Pedir o valor ao usuário (input) Mostrar o desconto em % também
valor = float(input("Digite o valor da compra: "))
#input() sempre retorna texto
#float() converte para número com decimal (ex: 1500.50)

if valor > 2000:
    desconto = valor * 0.20
    percentual = 20
elif valor > 1000:
    desconto = valor * 0.10
    percentual = 10
else:
    desconto = 0
    percentual = 0

valor_final = valor - desconto
print ("Valor da compra:", valor)
print ("Desconto aplicado:", percentual, "%")
print ("Valor do desonto:", desconto)
print ("Valor final:", valor_final)

#Isso se chama f-string 
print(f"Desconto aplicado: {percentual}%")