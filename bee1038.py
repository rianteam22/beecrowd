
listaValores = [4.00, 4.50, 5.00, 2.00, 1.50]
val, quant = input('').split(" ")

print(f'Total: R$ {listaValores[int(val)-1]*int(quant):.2f}')
