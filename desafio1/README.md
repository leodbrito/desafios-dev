### 1 - Decode URL

Dada uma *URL*, desenvolva um programa que indique se a URL é válida ou não e, caso seja válida, retorne as suas partes constituintes.


**Cenários de Teste**

> 1. Entrada: `https://globoesporte.globo.com/`
> 2. Saída
>   -  protocolo: https
>   -  host: globoesporte
>   - domínio: globo.com



> 1. Entrada: `http://www.google.com/mail/user=fulano`
> 2. Saída
>   - protocolo: http 
>   - host: www 
>   - domínio: google.com 
>   - path: mail 
>   - parâmetros: user=fulano



> 1. Entrada: `ssh://fulano%senha@git.com/`
> 2. Saída 
>   - protocolo: ssh 
>   - usuário: fulano 
>   - senha: senha 
>   - dominio: git.com

# Executando:

- `make run` ou `python desafio1.py`