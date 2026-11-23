# Código Python:
vtotal = float(input("Informe o valor total da compra: R$"))
quant = int(input("Quantidade de itens comprados: "))

print("Tem direito ao benefício:", vtotal>150 and quant>3)
