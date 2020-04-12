# Conversor de moedas
# Desenvolvido por Fábio de Almeida Martins

print("CONVERSOR DE MOEDAS")
menu = True
cot = ""
while menu:
    print("""\nMENU

(1) = Conversão de real para dólar
(2) = Conversão de dólar para real
(0) = Sair
""")
    resp = input("Selecione a opção desejada: ")
    if (resp == "1" or resp == "2"):
        if cot == "":
            cot = round(float(input("\nInsira a cotação atual do dólar para R$1,00: ")), 2)
        if resp == "1":
            x = round(float(input("\nInsira o valor a ser calculado (em R$): ")), 2)
            print("\nO valor em dólares é US$", round(x * cot, 2))
        elif resp == "2":
            x = round(float(input("\nInsira o valor a ser calculado (em US$): ")), 2)
            print("\nO valor em reais é R$", round(x / cot, 2))
        print("Retornando ao menu.")
    else:
        if resp != "0":
            print("\nOpção inválida.")
        else:
            menu = False
print("\nFinalizando.")
exit()
