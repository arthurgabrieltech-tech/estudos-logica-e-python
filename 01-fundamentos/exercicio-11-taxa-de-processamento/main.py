# Código em Python:
valor_transf = float(input("Informe o valor da transferência: R$"))

if valor_transf > 1000:
  valor_transf = valor_transf + 15
print(f"Valor da transferência bancária atualizada: R${valor_transf:.2f}")
