# Desafio 5.2 - Programação da Solução
#
# Usando o **desafio 5.1**, desenvolva o método GET da sua proposta.
# 
# Neste segundo desafio *pode* fazer **apenas a integração do serviço**, o caminho feliz, pega-lá-dá-cá. 
# Não precisa se preocupar com re-tentativas, tratamento de erros, etc. Somente o caminho feliz!
# 
# Criado em 30/01/2020
# Autor: Leonardo Ferreira de Brito <leonardo.brito@g.globo>
from flask import Flask, request
import requests


app = Flask(__name__)

@app.route('/')
def api():
    endpoint = 'https://randomprofile.com/api/api.php'
    response = requests.get(endpoint, params = request.args.to_dict())
    return response.text

if __name__ == '__main__':
    app.run(debug=True)