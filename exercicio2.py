# Criar uma lista chamada frutas com pelo menos 5 frutas Mostre:
#A lista completa
#A terceira fruta da lista
#A quantidade de frutas na lista
#Adicione uma nova fruta à lista
#Mostre a lista atualizada 

frutas = ["maçã", "banana", "uva", "laranja", "manga"]
print("Lista completa:", frutas)
print("Terceira fruta:", frutas[2])
print("Quantidade de frutas:", len(frutas))
 # len() conta quantos itens existem na lista
frutas.append("abacaxi")
#append() adiciona um item no final da lista
print("Lista atualizada:", frutas)

#Remova uma fruta da lista e mostre o resultado final
frutas.remove("banana")
print("Lista atualizada:", frutas)
