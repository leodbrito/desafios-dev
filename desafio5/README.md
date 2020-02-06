/### 5.1 - Análise de Problema e Solução

Você recebeu como tarefa desenvolver um serviço que faça a integração com o serviço Random Profile (https://randomprofile.com).
Os detalhes dessa API estão descritos em https://randomprofile.com/api-for-developers.

Este serviço tem 2 métodos: um `GET` que retorna um perfil e um `POST` que salva um novo perfil.
Neste primeiro desafio, você deve apresentar *uma descrição ou um desenho* (nada de código por enquanto!) de como você acha que deveria ser esta solução.

Uma dica: **NESTE PRIMEIRO DESAFIO**, este serviço pode prever algumas premissas como validações, timeout, re-tentativa, tratamento de erros, etc.



### 5.2 - Programação da Solução

Usando o **desafio acima**, desenvolva o método GET da sua proposta.

Neste segundo desafio *pode* fazer **apenas a integração do serviço**, o caminho feliz, pega-lá-dá-cá. 
Não precisa se preocupar com re-tentativas, tratamento de erros, etc. Somente o caminho feliz!

Após terminar, commite o seu código.

Outra dica: nós iremos avaliar a estrutura do seu código e como você se mantem focado no que foi pedido. Cuide da estrutura, entregue com qualidade!

Para este desafio será necessário um descritivo de como funciona a sua API, como levantar este serviço e como procerder com as chamadas.


## Rota "/"
A rota "/" faz a integração com a API Random Profile e retorna um perfil randômico de acordo com os parâmetros necessários seguindo as premissas descritas em https://randomprofile.com/api-for-developers.

Field name (\* for required) | Description
----------------------------|--------------
format                      | The format in which you want the results to be returned. We currently support these options:
* xml
* csv
* json
xml is chosen by default
----------------------------|--------------
countries *                 | A list of ISO 3 codes separated by a comma. Example: CHN,JPN. We currently support the following country codes:
* CHN
* GBR
* JPN
* KOR
----------------------------|--------------
packages                    | A list of package IDs separates by comma. The following packages are currently available:
* General (name, address, phone, date of birth etc.)
* Financial (bank account, credit card details, income etc.)
* Physical (height, weight, clothes size etc.)
By default the General package is selected.
----------------------------|--------------
fromAge                     | The minimum age in years for a profile. From 0 to 100. The default value is 0.
toAge                       | The maximum age in years for a profile. From 0 to 100. The default value is 100.
fullChildren                | 1 or 0
This is a flag that determines whether profiles with age under 18 years old can be assigned an occupation other than "Child" and bank details, such as randomly generated bank account number or credit card number.


# Setup:

- `make setup`

# Executando:

- `make run` ou `python desafio5.2.py`