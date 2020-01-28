# Desafio 3 - Intervalo de Números
#
# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
# 
# **Exemplo**:
# 
#  - Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
#  - Saída: [100-105], [110-111], [113-115], [150]
# 
# Criado em 27/01/2020
# Autor: Leonardo Ferreira de Brito <leonardo.brito@g.globo>
import re

def main():
    is_number_list = False
    while is_number_list == False:
        number_list = str(input('Informe uma lista de números: ')).strip()
        n_list = re.split(r'[, |]', number_list)
        false_list = []
        work_list = []
        for n in n_list:
            if n != '' and n.strip().isnumeric() == False:
                false_list.append(False)
            elif n!= '':
                work_list.append(int(n))
        if False in false_list:
            print(f'''\nLista inválida, digite apenas números, utilize vírgulas
             \rou espaços para separar os números e tente novamente!\n''')
        else:
            is_number_list = True
    work_list.sort()
    print(f'\nlista informada: {work_list}')


if __name__ == '__main__':
    main()