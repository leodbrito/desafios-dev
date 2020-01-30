# Desafio 4 - Troco
#
# Funcionários de empresas comerciais que trabalham como caixa tem uma grande 
# responsabilidade em suas mãos. A maior parte do tempo de seu expediente de 
# trabalho é gasto recebendo valuees de clientes e, em alguns casos, fornecendo change.
# 
# Seu desafio é fazer um programa que **leia o value total** a ser pago e o 
# **value efetivamente pago**, respondendo o **value do change** e o **menor número de 
# cédulas e moedas** que devem ser fornecidas.
# 
# Deve-se considerar que há:
# 
# > - cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00;
# > - moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05.
# 
# **Exemplos**:
# 
# > 1. Valor a ser pago: R$25,00
# > 2.  Valor efetivamente pago: R$40,00
# > 3. Troco: R$15,00
# > - 1 x R$ 10,00
# > - 1 x R$ 5,00
# 
# Criado em 27/01/2020
# Autor: Leonardo Ferreira de Brito <leonardo.brito@g.globo>

def main():
    change = Change(0.85,100)
    change.show_change()
    print(f'\n')
    change = Change(0.85,50)
    change.show_change()
    
class Change:
    def __init__(self, cost, amount_payed, change = None, money = None):
        self.cost = cost 
        self.amount_payed = amount_payed
        self.change = change
        self.money = money
    
    def show_change(self):
        change = self.change
        cost = self.cost
        amount_payed = self.amount_payed
        money = self.money
        output = f'''
                 \r1. Valor a ser pago: R$ {cost:.2f}
                 \r2. Valor efetivamente pago: R$ {amount_payed:.2f}
                 \r3. Troco: R$ {change:.2f}\n'''
        values_list = []
        if self.change != 0:
            # definindo uma lista de valores de troco (cédulas e moedas)
            while change > 0:
                for value in self.money:
                    if value <= change:
                        values_list.append(value)
                        change -= value
                        change = round(change, 2)
                        break
            i = 1
            # Agrupando a lista de valores de troco (cédulas e moedas) em um dicionário
            values_dict = {}
            for value in values_list:
                if value == values_list[0]:
                    if value in values_dict.keys():
                        values_dict[value] += 1
                    else:
                        values_dict[value] = 1
                elif i < len(values_list) and value == values_list[i-1]:
                    if value in values_dict.keys():
                        values_dict[value] += 1
                    else:
                        values_dict[value] = 1
                else:
                    values_dict[value] = 1
                i += 1
            # formatando a saída stdout
            for k,v in values_dict.items():
                output += f'- {v} x R$ {k:.2f}\n'
        print(f'\n{values_list}\n{output}')

    @property
    def change(self):
        return self._change

    @change.setter
    def change(self, value):
        value = round(float(self.amount_payed) - float(self.cost),2)
        self._change = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        value = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
        self._money = value

if __name__ == '__main__':
    main()