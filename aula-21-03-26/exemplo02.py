pagamento = float(input("digite o valor do pagamento:"))
valor_com_juros =pagamento*1.2 if pagamento >= 457.67 else pagamento*1.1
print (f'o prejuizo foi de R${valor_com_juros}')
