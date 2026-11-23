# Código Python:
nasc = int(input("Digite seu ano de nascimento (XXXX): "))
atual = int(input("Digite o ano atual (YYYY): "))
idade = atual - nasc

print("Idade:", idade)
print("Maior de idade:", (idade>=18))
