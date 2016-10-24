# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1. [Aula2](#aula2)  
1.2. [Alteração do settings.py](#alteração-do-settingspy)  

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Caso o Virtualenv não esteja ativado, ative-o: pelo _terminal_ do Linux, em seu diretório ```py3.5$``` ative o virtualenv,  por meio do comando
```sh
py3.5$ source ./bin/activate
(py3.5)tmenegaz@tam:~/Documentos/aulaDjango/py3.5$
```
Caso não esteja conforme acima volte para [Comandos de ativação do ambiente](#comandos-de-ativação-do-ambiente)  e refaça o processo.

---

## Aula2
[Voltar ao topo(Conteúdo)](#conteúdo)  
O segundo projeto terá o nome _aula2_ e, da mesma forma que o [_aula1_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5/aula1),  um conjunto de pastas e arquivos gerados automaticamente pelo Django. Em seu diretório ```py3.5$``` digite o comando abaixo para criar seu projeto Django.
```sh
py3.5$ django-admin startproject aula2
```
> No _cmd_ do Windows digite
```cmd
py3.5>django-admin startproject aula2
```

Se quiser teste seu projeto da mesma forma que voi feito anteriormente, corregue-o no _browser_ por meio do comando ```./manage.py runserver```. Tudo funciona bem!

Por meio da barra de ferramentas do ```Atom```: ```File/Open Folder``` selecione a pasta ```aula2``` e clique em ```ok```.

O projeto [_aula2_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5) tem a mesma estrutura do projeto [_aula1_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5). O que faremos é aproveitar essa estrutura para criar a nossa própria _view_ e indicar o caminho pela _urls_ para que o _browser_ encontre o conteúdo da _view_. Nesse caso testaremos se o _navegador_ retorna na tela a frase **Hello World!**. Esse processo será, em um primeiro momento, construido sem a modularização ofericida como padrão pela instrução ```django-admin```. Aqui, nesse momento, aglutina-se a _view_ no arquivo _settings.py_. O que se quer com isso é mostrar a grande capacidade de acoplamento do Python para trechos de códigos que podem ser reunidos em um arquivo ou em arquivos distintos. Isso é possível, em _Python_, sem demandar esforços para além da _sintaxe_ da Linguagem.

---

# Alteração do settings.py
[Voltar ao topo(Conteúdo)](#conteúdo)  
O que se busca com essa forma de acesso é apresentar meios de associar as funções da ```views```, da ```urls``` e do ```settings``` sem criar uma situção de dependência. Contudo, essa forma de inserir a ```views``` no arquivo ```settings``` contraria totalmente a ideia de não dependência.

Dito isso, o que se tem é uma mecaniso didático para mostrar ao estudante a semântica do processo de criação da views.

O que foi feito consiste em criar a função ```helloWorld``` no final do arquivo ```settings```. A sintaxe da função pode ser vista abaixo:
```py
from django.http import HttpResponse
def helloWorld(request):
    return HttpResponse("Hello World!")
```
Inportou-se a classe ```HttpResponse``` do módulo ```http``` para solicitar ao servidor uma resposta por meio de um pedido ```(request)```. Com isso o servidor retorna uma resposta, por meio do construtor da classe. Esse construtor que recebeu uma ```str``` ```Hello World``` como argumento. Nesse caso, a resposta será o argumento do construtor.

Para que o servidor encontre o caminho da solicitação é preciso indicar o endereço e o nome da função que contém os parâmetros do protocolo ```http```. Isso é feito no arquivo ```urls.py```, por meio do código abaixo:
```py
from django.conf.urls import url
from . import settings
urlpatterns = [
    url(r'^$', settings.helloWorld),
]
```
No trecho de código apresentado para a ```urls.py``` importa-se o módulo ```url``` e o módulo ```settings.py``` para indexá-los na ```list``` ```urlpatterns```. dessa forma a função ```url``` passa como argumentos à seus atributos:
1. uma expressão regular que indica que o diretório raiz trará o conteudo;
2. o módulo e a função que contém o conteúdo proposto.

É possível ainda passar um 3º argumento. Nesse caso não foi enviado. Ele serve para incicar na url do navegador o nome que se quer exibir para o caminho e o arquivo que contém oconteúdo.

Teste seu projeto como da outra vez: corregue-o no _browser_ por meio do comando ```./manage.py runserver```. O que será visto é o conteúdo ```Hello Horld!```.

Para a [_aula3_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5) vamos criar nossa primira página ```html``` com ```css``` externo para ilustrar uma aplicação.

---

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
