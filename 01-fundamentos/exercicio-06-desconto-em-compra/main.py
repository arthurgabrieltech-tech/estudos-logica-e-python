vtotal = float(input("Informe o valor total: R$"))

if vtotal>200:
  vtotal = vtotal - 30
print(f"Valor total a pagar: R${vtotal:.2f}")
