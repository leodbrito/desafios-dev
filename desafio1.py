# Desafio 1
import re

class Url:
    def __init__(self, url, protocol=None, host=None, domain=None, \
                path=None, parameters=None, user=None, password=None):
        self.url = url
        self.protocol = protocol
        self.host = host
        self.domain = domain
        self.path = path
        self.parameters = parameters
        self.user = user
        self.password = password

    def validateurl(self):
        test_url = re.findall(r'^(http[s]?://\w+\.\w+\.?\w*|ssh://\w+%.+@\w+\.\w+)',self.url)
        if not test_url:
            return f'URL inválida!'
        else:
            return True
            

    def split_url(self):
        urlsplited = re.split('://|[:./@]',self.url)
        return urlsplited

    def proccess_properties(self):
        properties = {
                        'url':self.url,
                        'protocol':'',
                        'host':'',
                        'domain':'',
                        'path' :'',
                        'parameters':'',
                        'user' :'',
                        'password':''
                     }
        if self.validateurl() == True:
            # Processando alguns atributos da classe dependendo se existe ou não http na URL
            properties['protocol'] = self.split_url()[0]
            if 'http' in self.url:
                properties['host'] = self.split_url()[1]
                domain = re.split('\.', self.url, 1)[1]
                domain = re.split('/', domain)[0]
                properties['domain'] = domain
                pattern = re.compile(r'/\w+/')
                path = pattern.findall(self.url)
                if len(path) > 0:
                    path = path[0].replace('/','')
                    properties['path'] = path
            else:
                pattern = re.compile(r'@.*')
                domain = pattern.findall(self.url)[0].split('/')[0]
                domain = domain.replace('@','')
                properties['domain'] = domain
            # Processando alguns atributos da classe sem depender se existe ou não http na URL
            for s in self.split_url():
                if '=' in s:
                    parameters = s
                    properties['parameters'] = parameters
                elif '%' in s:
                    user = s.split('%')[0]
                    properties['user'] = user
                    password = s.split('%')[1]
                    properties['password'] = password
        return properties

    def show_url_decodded(self):
        for k,v in self.proccess_properties().items():
            if v != '' and v != None:
                print(f'{k.capitalize()}: {v}')

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        value = self.split_url()[0]
        self._protocol = value
    
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        value = self.proccess_properties()['host']
        self._host = value
    
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        value = self.proccess_properties()['domain']
        self._domain = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        value = self.proccess_properties()['path']
        self._path = value

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        value = self.proccess_properties()['parameters']
        self._parameters = value
     
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        value = self.proccess_properties()['user']
        self._user = value
        
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        value = self.proccess_properties()['password']
        self._password = value


#url=str(input('Iforme uma URL: ')).strip()
url="https://www.globo.com/path/nada/"
u = Url(url)
print(u.validateurl())
print(u.split_url())
print(u.show_url_decodded())
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
print(u2.validateurl())
print(u2.split_url())
print(u2.show_url_decodded())
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
print(u3.validateurl())
print(u3.split_url())
print(u3.show_url_decodded())
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
print(u4.validateurl())
print(u4.split_url())
print(u4.show_url_decodded())
#print(f'Protocolo : {u4.protocol}')
#print(f'Host : {u4.host}')
#print(f'Domínio : {u4.domain}')
#print(f'Path ; {u4.path}')
#print(f'Parametros : {u4.parameters}')
print(f'Usuário : {u4.user}')
print(f'Senha : {u4.password}')
print('\n')

url="ftp://host.dominio"
u5 = Url(url)
print(u5.validateurl())
print('\n')

url="https://www."
u6 = Url(url)
print(u6.validateurl())
print('\n')