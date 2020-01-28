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
    is_numbers_list = False
    while is_numbers_list == False:
        numbers_list = str(input('Informe uma lista de números: ')).strip()
        nl = NumbersList(numbers_list)
        is_numbers_list = nl.validate()
    nl.show_groupped()

class NumbersList:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def validate(self):
        numbers_list = re.split(r'[, |]', self.numbers_list)
        false_list = []
        work_list = []
        for number in numbers_list:
            if number != '' and number.strip().isnumeric() == False:
                false_list.append(False)
            elif number != '':
                work_list.append(int(number))
        if False in false_list:
            return False
        else:
            work_list.sort()
            return work_list
    
    def group_numbers_list(self):
        if self.validate() != False:
            work_list = self.validate()
            wl_i = 0
            nl_i = 0
            groupped_list = []
            for number in work_list:
                if number == work_list[0]:
                    groupped_list.append([number])
                elif number - 1 == work_list[wl_i-1]:
                    groupped_list[nl_i].append(number)
                else:
                    nl_i += 1
                    groupped_list.append([number])
                wl_i += 1
            return groupped_list

    def show_groupped(self):
        output_list = []
        output = ''
        for n_list in self.group_numbers_list():
            last_index_n_list = len(n_list)-1
            if n_list[0] == n_list[last_index_n_list]:
                output_list.append(f'[{n_list[0]}]')
            else:
                output_list.append(f'[{n_list[0]}-{n_list[last_index_n_list]}]')
        for item in output_list:
            if item == output_list[0]:
                output += f'{item}'
            else:
                output += f', {item}'
        print(f'\n{output}\n')

if __name__ == '__main__':
    main()