codigopeca,numeropeca,valorpeca = input().split()
codigopeca2,numeropeca2,valorpeca2 = input().split()

codigopeca = int(codigopeca)
numeropeca = int(numeropeca)
valorpeca = float(valorpeca)
codigopeca2 = int(codigopeca2)
numeropeca2 = int(numeropeca2)
valorpeca2 = float(valorpeca2)

valor = numeropeca * valorpeca
valor2 = numeropeca2 * valorpeca2
resultado = valor + valor2

print("VALOR A PAGAR: R$ %.2f" % resultado)