# Desafio 1 - Decode URL
# Dada uma *URL*, desenvolva um programa que indique se a URL
# é válida ou não e, caso seja válida, retorne as suas partes constituintes.
# Criado em 23/01/2020
# Autor: Leonardo Ferreira de Brito <leonardo.brito@g.globo>
import re

def main():
    url = str(input('Informe uma URL: ')).strip()
    u = Url(url)
    print(f'\n{u.validate_url()}\n')
    u.show_url_decodded()

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

    def validate_url(self):
        test_url = re.findall(r'^(http[s]?://\w+\.\w+\.?\w*|ssh://\w+%.+@\w+\.\w+)',self.url)
        if not test_url:
            return f'URL inválida!'
        else:
            return f'URL válida!'
            

    def split_url(self):
        urlsplited = re.split('://|[: /@]',self.url)
        return urlsplited

    # método para gerar um dicionário com os atributos da classe
    def proccess_properties(self):
        properties = {
                        'protocol':'',
                        'host':'',
                        'domain':'',
                        'path' :'',
                        'parameters':'',
                        'user' :'',
                        'password':''
                     }
        if self.validate_url() == 'URL válida!':
            # Processando alguns atributos da classe dependendo se existe ou não http na URL
            url_splitted = self.split_url()
            properties['protocol'] = url_splitted[0]
            for item in url_splitted:
                if '.' in item and 'http' in self.url:
                    properties['host'] = url_splitted[1].split('.')[0]
                    properties['domain'] = url_splitted[1].replace(properties["host"]+'.','')
                elif '.' in item:
                    properties['domain'] = item
                elif '=' in item:
                    parameters = item
                    properties['parameters'] = parameters
                elif '%' in item:
                    user = item.split('%')[0]
                    properties['user'] = user
                    password = item.split('%')[1]
                    properties['password'] = password
                elif url_splitted[0] not in item:
                    properties['path'] = item
        return properties

    def show_url_decodded(self):
        for k,v in self.proccess_properties().items():
            if v != '' and v != None:
                print(f' - {k.capitalize()}: {v}')
        print(f'\n')

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

if __name__ == '__main__':
    main()