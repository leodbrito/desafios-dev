 ### Desafio 5.1 - Análise de Problema e Solução

 Você recebeu como tarefa desenvolver um serviço que faça a integração com o serviço Random Profile (https://randomprofile.com).
 Os detalhes dessa API estão descritos em https://randomprofile.com/api-for-developers.
 
 Este serviço tem 2 métodos: um `GET` que retorna um perfil e um `POST` que salva um novo perfil.
 Neste primeiro desafio, você deve apresentar *uma descrição ou um desenho* (nada de código por enquanto!) 
 de como você acha que deveria ser esta solução.
 
 Uma dica: **NESTE PRIMEIRO DESAFIO**, este serviço pode prever algumas premissas como validações, timeout, 
 re-tentativa, tratamento de erros, etc.
 
 
 ### Resposta:

 O serviço consistirá em um Framework Web e um serviço de Banco de Dados, deverá possuir 1 classe representando
 o perfil "General" da API Random Profile. Essa classe também será uma entidade no Banco e servirá como modelo para, 
 quando instanciada, receber os atributos do perfil para exibi-los, através método GET ou salvá-los no Banco, através 
 do método POST. Quando o serviço estiver UP, ao receber uma requisição GET com os devidos parâmetros, estes são validados
 e em seguinda uma nova requisição GET é feita na API Random Profile que por sua vez retornará um perfil randômico que 
 será exibido na tela. Já ao receber uma requisição POST, o mesmo processo do GET é feito, porém ao invés de exibir na 
 tela, o perfil será salvo no Banco. A cada requisição feita na API Random Profile haverá um timeout de 3 segundos e após 
 uma única retentativa se não existir retorno, uma mensagem  de erro 404 com um texto informativo será exibida.