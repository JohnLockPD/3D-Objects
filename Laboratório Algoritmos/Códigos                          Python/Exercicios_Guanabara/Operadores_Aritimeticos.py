NumberOne = int(input("Digite um numero:"))
NumberTwo = int(input("Digite outro numero:"))
soma = (NumberOne+NumberTwo)
subtracao = (NumberOne-NumberTwo)
multiplicacao = (NumberOne*NumberTwo)
divisao = (NumberOne//NumberTwo)
potencia = (NumberOne**NumberTwo)
print(" A soma: {}.\n A diferença: {}.\n O produto: {}.\n A divisão inteira: {}.\n A potência: {:.3f}".format(
    soma, subtracao, multiplicacao, divisao, potencia))
