
import os

while True:
    print('******************************************************************************************')
    print('                   Sistema de registro de datos Python Utel')
    print('******************************************************************************************')

    name = input('Ingresa nombre ')
    corre = input('correo electronico ')
    email = input('tel ')

    print(' \n',name,' \n',corre,' \n',email)

    s = input('Quieres salir del programa Y/N')

    if s=='Y':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

print('******************************************************************************************')

