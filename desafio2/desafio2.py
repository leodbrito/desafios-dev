# Desafio 2 - Happy Number
#
# Para saber se um número é feliz, você deve obter o quadrado
# de cada dígito deste número, em seguida você faz a soma desses
# resultados. A seguir o mesmo procedimento deve ser feito com o
# valor resultante desta soma. Se ao repetir o procedimento diversas
# vezes obtivermos o valor 1, o número inicial é considerado feliz.
#
# Tomamos o 7, que é um **número feliz**:
# 
# - 7² = 49
# - 4² + 9² = 97
# - 9² + 7² = 130
# - 1² + 3² + 0² = 10
# - 1² + 0² = 1
#
# Podemos observar nesse exemplo que os números **49, 97, 130 e 10**
# também são felizes. Existem infinitos números felizes.
# E um número triste? Como sabemos que um número não será feliz?
# Desenvolva um programa que determine se um número é feliz ou triste.
# 
# Criado em 25/01/2020
# Autor: Leonardo Ferreira de Brito <leonardo.brito@g.globo>

def main():
    num = ''
    while num.isnumeric() == False:
        num = input('Informe um número para descobrir se ele é feliz: ')
        if num.isnumeric() == False:
            print('Digito inválido, tente novamente!')
    number = Number(num)
    output = ''
    result = 0
    while result != 1:
        total_digits = number.total_digits
        digit_list = number.convert_digit_list()
        for digit in digit_list:
            if total_digits == 1:
                output += f' - {digit}²'
            else:
                if digit_list.index(digit) == 0:
                    output += f' - {digit}²'
                elif digit_list.index(digit) == digit_list[len(digit_list)-1]:
                    output += f' + {digit}² ='
                else:
                    output += f' + {digit}²'
        result = number.sum_square_digits()
        output += f' = {result}\n'
        if result == 4 or result == 0:
            print(f'\nO numero {num} é triste!\n')
            break
        number = Number(result)
    if result == 1:
        print(f'\nO numero {num} é feliz!\n')
    print(output)

class Number:
    def __init__(self, num, total_digits = None):
        self.num = num
        self.total_digits = total_digits

    def convert_digit_list(self):
        digit_list = [int(i) for i in str(self.num)]
        return digit_list

    def sum_square_digits(self):
        result = 0
        i = 0
        for digit in self.convert_digit_list():
            result += self.convert_digit_list()[i] ** 2
            i += 1
        return result

    @property
    def total_digits(self):
        return self._total_digits

    @total_digits.setter
    def total_digits(self, value):
        value = len(self.convert_digit_list())
        self._total_digits = value

if __name__ == '__main__':
    main()

