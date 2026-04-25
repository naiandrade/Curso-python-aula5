#Resolva - o cliente vai fazer uma compra e se for acima de 1000 ele recebe 10% de desconto,
#e se for acima de 2000 ele recebe 20% de desconto.

valor = 1600
if valor > 2000:
    desconto = valor * 0.20
elif valor > 1000:
    desconto = valor * 0.10
else:
    desconto = 0

total_com_desconto = valor - desconto
print ("Valor da compra:", valor)
print ("deconto:", valor)
print ("Valor final:", total_com_desconto)

#if → primeira condição
#elif → outra condição
#else → caso nenhuma seja verdadeira
