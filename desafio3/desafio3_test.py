# Arquivo para testes do desafio3
import re

def main():
    number_list = 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
    str(number_list)
    print(number_list)
    while not re.split(r'[, |]',number_list):
        print('Lista inválida, utilize "," ou "espaço" para separar os números e tente novamente!')
    n_list = re.split(r'[, |]',number_list)
    print(n_list)
    

    


if __name__ == '__main__':
    main()