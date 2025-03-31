while True:
    num = int(input('Digite um número, para ver a tabuada dele: '))
    if num < 0:
        break
    else:
        for c in range(1,11):
            tabuada = num * c
            print(f'{num} x {c} = {tabuada}')
print('Programa Finalizado')
