# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1. [Aula3](#aula3)  
1.2. [Alteração do settings.py](#alteração-do-settingspy)  

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Evidentemente que você notou o comando ```python manage.py startapp [app_label]``` quando rodou o seu projeto aula1 ou testou aula2 e aula3, após executar o comando ```manage.py runserver``` pela primeira vez, em cada projeto. Esse comando cria para seu projeto os diretórios e arquivos necessários para sua aplicação. Ainda não será utilizada a linha de código acima. Entende-se ser razoável a criação de uma estrutura sem comandos ou com o mínimo possível afim de proporcionar um melhor entendimento da arquitetura do _Django_ nos projetos. Aqui será criado um modelo semelhante ao do comando para dar condições de preservar a modularização, mesmo que de forma parcial no projeto. Serão criados diretórios e arquivos com a disposições específicas.

---

## Aula3
[Voltar ao topo(Conteúdo)](#conteúdo)  
Com o _Virtualenv_ ativado crie seu projeto. Caso existam dúvudas, ainda, quanto a ativação e criação do projetos consulte o material do _projeto_ em [_aula1_](https://github.com/tmenegaz/django/blob/master/projeto1.md#o-projeto).

O projeto _aula3_ terá arquivos _estáticos_, uma views e um _urls_ configurado para acessar o conteúdo do página com a estilização determinada.

Primeiro crie as pastas e diretórios abaixo
```sh
  aula3
│   ├── templates
│   │   └── aula3
│   │       ├── css
│   │       │   └── skyn.css
│   │       └── index.html
```

O Django classifica arquivos com extensão ```jpg```, ```css```, ```html```, ```js``` _etc_ como estáticos. Esses arquivos serão explorados na medida em que houver demandas. Para cada um dos arquivos, crie elementos _tags_ básicos e _seletores_ correspondentes para testar sua aplicação.

Em ```$ aula3/templates/aula3/css/``` crie um arquivo ```skyn.css``` com os seguintes seletores:
 ```css
 @charset "UTF-8";
body {
    background-color: #000;
}
h1 {
    color: #fff;
}
 ```

Em ```$ aula3/templates/aula3/```, crie um arquivo chamado ```index.html``` com as seguintes _tags_:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/skyn.css">
    <title>Index</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

Em ```$ aula3/aula3/``` crie  seu arquivo ```views.py``` com as seguintes funções:
```py
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'aula3/index.html',{})
def OlaMundo(request):
    return HttpResponse("Olá mundo!")
def status_code(request):
    return HttpResponse("Resposta %s" % (HttpResponse.status_code))
```
As funções de _Python_ no arquivo ```views.py``` tem suas ações bem definodas: Solicitar ao servidor _Web_ - ```request``` -  e receber a resposta do servidor - ```response```. As respostas podem ser o conteúdo em uma página ```html```, uma imagem, um vídeo, um audio, um _erro_ _404_, um arquivo ```xml``` ou, de fato, qualquer coisa que esteja no servidor. Em verdade, essa funções poderiam estar em qualquer arquivo, mas convencionou-se chamar esse arquivo de ```views.py```.
No trecho de código acima são importadas a classe _HttpResponse_ e a função _render_. A classe é utilizada para obter uma resposta do servidor, neste caso a ```str``` passada como argumanto em seu construtor. A função _render_ acessa e renderiza uma página a partir do topo da árvore do seu diretório em _templates_. portanto, receberá o conteúdo da página ```index.html```.  

Na ```urls.py``` digite conforme abaixo:
```py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ola/mundo/$', views.OlaMundo, name='olaMundo'),
    url(r'^status/$', views.status_code, name='status_code'),
]
```
O arquivo que mapeia as rotas para o ```views.py``` é o arquivo ```urls.py```.
Ele tem a função de fazer a ponte da ```views.py``` com o ```settings.py``` por maio da constante ```ROOT_URLCONF = 'aula3.urls'```, em ```settings.py```.

Após criar os diretórios e arquivos, o seu projeto terá a seguinte disposição:
```py
./aulaDjango/py3.5/aula3
├── aula3
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   ├── views.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── templates
│   │   └── aula3
│   │       ├── css
│   │       │   └── skyn.css
│   │       └── index.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---

# Alteração do settings.py  
[Voltar ao topo(Conteúdo)](#conteúdo)  
A única alteração necessária no arquivo ```settings.py``` será acrescentar ```aula3``` no final da lista da constante ```INSTALLED_APPS```, conforme abaixo:
 ```py
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # meus app em templates
    'aula3',
]
```
Dessa forma indicamos ao _Django_ que temos uma aplicação própria, não padrão. Isso quer dizer que nossa aplicação pode ser compatível com a regra de negócio proposta a partir de um fato concreto.
O projeto está pronto e todo o código pode ser acessado e modificado. Clique em  [aula3](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5/aula3).

Com isso chega ao fim a oficina para divulgação e apresentação do Framework _Django_ que ocorreu no _MundoSenai_.

---

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
