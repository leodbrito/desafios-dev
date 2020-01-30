# Arquivo para testes do desafio1

from desafio1 import Url

url="https://www.globo.com/path"
u = Url(url)
print(u.validate_url())
print(u.split_url())
u.show_url_decodded()
#print(f'Protocolo : {u.protocol}')
#print(f'Host : {u.host}')
#print(f'Domínio : {u.domain}')
#print(f'Path ; {u.path}')
#print(f'Parametros : {u.parameters}')
#print(f'Usuário : {u.user}')
#print(f'Senha : {u.password}')
print('\n')

url="http://globoesporte.globo.com"
u2 = Url(url)
print(u2.validate_url())
print(u2.split_url())
u2.show_url_decodded()
#print(f'Protocolo : {u2.protocol}')
#print(f'Host : {u2.host}')
#print(f'Domínio : {u2.domain}')
#print(f'Path ; {u2.path}')
#print(f'Parametros : {u2.parameters}')
#print(f'Usuário : {u2.user}')
#print(f'Senha : {u2.password}')
print('\n')

url="http://www.google.com/mail/user=fulano"
u3 = Url(url)
print(u3.validate_url())
print(u3.split_url())
u3.show_url_decodded()
#print(f'Protocolo : {u3.protocol}')
#print(f'Host : {u3.host}')
#print(f'Domínio : {u3.domain}')
#print(f'Path ; {u3.path}')
#print(f'Parametros : {u3.parameters}')
#print(f'Usuário : {u3.user}')
#print(f'Senha : {u3.password}')
print('\n')

url="ssh://fulano%senha@git.com/"
u4 = Url(url)
print(u4.validate_url())
print(u4.split_url())
u4.show_url_decodded()
#print(f'Protocolo : {u4.protocol}')
#print(f'Host : {u4.host}')
#print(f'Domínio : {u4.domain}')
#print(f'Path ; {u4.path}')
#print(f'Parametros : {u4.parameters}')
print('\n')

url="ftp://host.dominio"
u5 = Url(url)
print(u5.validate_url())
print('\n')

url="https://www."
u6 = Url(url)
print(u6.validate_url())
print('\n')