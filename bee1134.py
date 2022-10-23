"""
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um
algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim).
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
(até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.
"""

# 1.Álcool 2.Gasolina 3.Diesel 4.Fim
tipo = 0
alc, gas, dis = 0, 0, 0

while tipo != 4:
    tipo = int(input(''))
    if tipo == 1:
        alc += 1
    elif tipo == 2:
        gas += 1
    elif tipo == 3:
        dis += 1
print(f'MUITO OBRIGADO\nAlcool: {alc}\nGasolina: {gas}\nDisel: {dis}')