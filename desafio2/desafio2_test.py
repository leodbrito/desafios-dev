# Arquivo para testes do desafio1
from desafio2 import Number

num = 0
n = Number(num)
print(f'{num}\nlista : {n.convert_digit_list()}')
print(f'total de digitos: {n.total_digits}')
print(f'{num}² = {n.square}\nsoma dos quadrados dos digitos: {n.sum_square_digits()}\n')

num = 3
n = Number(num)
print(f'{num}\nlista : {n.convert_digit_list()}')
print(f'total de digitos: {n.total_digits}')
print(f'{num}² = {n.square}\nsoma dos quadrados dos digitos: {n.sum_square_digits()}\n')

num = 7
n = Number(num)
print(f'{num}\nlista : {n.convert_digit_list()}')
print(f'total de digitos: {n.total_digits}')
print(f'{num}² = {n.square}\nsoma dos quadrados dos digitos: {n.sum_square_digits()}\n')

num = 10
n = Number(num)
print(f'{num}\nlista : {n.convert_digit_list()}')
print(f'total de digitos: {n.total_digits}')
print(f'{num}² = {n.square}\nsoma dos quadrados dos digitos: {n.sum_square_digits()}\n')

num = 103
n = Number(num)
n.num = 105
print(f'{num}\nlista : {n.convert_digit_list()}')
print(f'total de digitos: {n.total_digits}')
print(f'{num}² = {n.square}\nsoma dos quadrados dos digitos: {n.sum_square_digits()}\n')