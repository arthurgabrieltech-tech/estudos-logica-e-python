sal = float(input("Salário do funcionário: R$"))

if sal < 1500:
  sal = sal + 200
print(f"Valor final do salário: R${sal:.2f}")
