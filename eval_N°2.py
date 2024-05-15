'''Este algoritmo automatiza el funcionamiento del stock de una tienda'''
import os

'''Definicion de el stock base y el menu principal'''
print('-'*50)
print('Administracion de stock de "Aqui Vendemos"'.center(50, '-'))
print('-'*50)
stock = {'harina': 3, 'huevos': 15, 'cafe': 1, 'leche': 4}
menup= ['Ver catalogo', 'Agregar producto', 'Eliminar producto', 'Modificar producto', 'Salir' ]
print()
while True:
    for ind, opcion in enumerate(menup):
        print(f'{ind + 1}. {opcion}')
    print()
    ans = input('Indique la opcion a realizar\n')
    if ans == '1':
        os.system('cls')
        for prod, cant in stock.items():
            print(f'{prod}: {cant}')
        print()
    elif ans == '2':
        os.system('cls')
        while True:
            newpr = input('¿Que producto desea ingresar al stock?\n')
            os.system('cls')
            newcant = int(input('Indique la cantidad del producto que desea ingresar\n'))
            if newpr.replace(' ', '').isalpha():
                break
        if newpr.lower() in stock:
            os.system('cls')
            print('Error: Producto ya en stock\n')
            continue
        else:
            os.system('cls')
            stock[newpr.lower()] = newcant
            print('Producto agregado exitosamente\n')
    elif ans == '3':
        os.system('cls')
        while True:
            cantdel = input('Ingrese el nombre del producto que desea eliminar\n')
            if cantdel.replace(' ', '').isalpha:
                break
        if cantdel.lower() in stock:
            os.system('cls')
            del stock[cantdel.lower()]
            print('Producto eliminado exitosamente\n')
        else:
            os.system('cls')
            print('Producto inexistente\n')
    elif ans == '4':
        os.system('cls')
        while True:
            prod = input(str('Ingrese el nombre del producto a modificar\n'))
            if prod.lower() in stock:
                val = input('ingrese el numero del nuevo stock\n')
            if prod.lower() in stock:
                stock.update({prod:val})
                os.system('cls')
                print(f'Nueva cantidad de {prod} actualizado/a a: {val}\n')
                break
            else:
                os.system('cls')
                print('Producto inexistente en stock\n')
    elif ans == '5':
        os.system('cls')
        exit('Adios!')
    else:
        os.system('cls')
        print('Error: opcion invalida\n')
