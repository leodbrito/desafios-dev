## desafios-dev
Para execução dos desafios é necessário ter instalado o Python, a partir da versão 3, e de preferência um ambiente virtual como o Virtualenv.

## Download e instalação do Python
Siga as instruções desse link: https://wiki.python.org/moin/BeginnersGuide/Download

## Instalação do Virtualenv
Siga as instruções do link: https://virtualenv.pypa.io/en/latest/installation.html

## Utilização
Efetue o "clone" do projeto:
-`git clone https://github.com/leodbrito/desafios-dev.git`

# Configure e Inicie o Virtualenv
Defina a versão do Python clolocando o PATH de instalação do binário no parâmetro "--python", conforme exemplo abaixo:
- `virtualenv --python=/opt/python-3.6/bin/python NOME_DO_AMBIENTE`

Inicie o ambiente na raíz do projeto, pois servirá para todos os desafios:
- `virtualenv NOME_DO_AMBIENTE\bin\activate` ou `.NOME_DO_AMBIENTE\bin\activate`

Para desligar o ambiente:
- `deactivate`