# Código Python
valor_compra = float(input("Informe o valor da compra: R$"))
valor_pago = float(input("Informe o valor pago: R$"))
troco = valor_pago
troco -= valor_compra
if valor_pago < valor_compra:
  print("Não foi possível efetuar o pagamento!")
else:
  print(f"O valor do troco será: R${troco:.2f}")
