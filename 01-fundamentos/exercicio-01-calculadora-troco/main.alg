 algoritmo "Calculadora de troco"

var
  valor_compra, valor_pago, troco: real
inicio
  escreval("Informe o valor da compra: R$")
  leia(valor_compra)
  escreval("Informe o valor pago: R$")
  leia(valor_pago)
  troco <- valor_pago - valor_compra
  se valor_pago < valor_compra entao
    escreva("Não foi possível realizar o pagamento!")
  senao
    escreva("O valor do troco será: R$", troco:4:2)
  fimse
fimalgoritmo
