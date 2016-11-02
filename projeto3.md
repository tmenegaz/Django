# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1. [Aula3](#aula3)  
1.2. [Alteração do settings.py](#alteração-do-settingspy)  
1.3. [Arquivos estáticos](#arquivos-estáticos)

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Evidentemente que você notou o comando ```python manage.py startapp [app_label]``` quando rodou o seu projeto aula1 ou testou aula2 e aula3, após executar o comando ```manage.py runserver``` pela primeira vez, em cada projeto. Esse comando cria para seu projeto os diretórios e arquivos necessários para sua aplicação. Ainda não será utilizada a linha de código acima. Entende-se ser razoável a criação de uma estrutura sem comandos ou com o mínimo possível afim de proporcionar um melhor entendimento da arquitetura do _Django_ nos projetos. Aqui será criado um modelo semelhante ao do comando para dar condições de preservar a modularização, mesmo que de forma parcial no projeto. Serão criados diretórios e arquivos com a disposições específicas.

---

## Aula3
[Voltar ao topo(Conteúdo)](#conteúdo)  
Com o _Virtualenv_ ativado crie seu projeto. Caso existam dúvudas, ainda, quanto a ativação e criação do projetos consulte o material do _projeto_ em [_aula1_](https://github.com/tmenegaz/django/blob/master/projeto1.md#o-projeto).

O projeto _aula3_ terá arquivos _estáticos_, uma views e um _urls_ configurado para acessar o conteúdo do página com a estilização determinada.

Primeiro crie os diretórios e arquivos abaixo em `aula3`
```sh
  ./
├── aula3
├── statics
│   └── css
│       └── skin.css
└── templates
    └── index.html

```

O Django classifica arquivos com extensão ```jpg```, ```css```, ```js``` _etc_ como estáticos e ```html``` como templates. Esses arquivos serão explorados na medida em que houver demandas. Para cada um dos arquivos, crie elementos _tags_ básicos e _seletores_ correspondentes para testar sua aplicação.

Em ```$ aula3/statics/css/``` crie um arquivo ```skin.css``` com os seguintes seletores:
 ```css
 @charset "UTF-8";
body {
    background-color: #000;
}
h1 {
    color: #fff;
}
 ```

Em ```$ aula3/templates/```, crie um arquivo chamado ```index.html``` com as seguintes _tags_:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/skyn.css" />
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
As funções de _Python_ no arquivo ```views.py``` tem suas ações bem definidas: Solicitar ao servidor _Web_ - ```request``` -  e receber a resposta do servidor - ```response```. As respostas podem ser o conteúdo em uma página ```html```, uma imagem, um vídeo, um audio, um _erro_ _404_, um arquivo ```xml``` ou, de fato, qualquer coisa que esteja no servidor. Em verdade, essa funções poderiam estar em qualquer arquivo, mas convencionou-se chamar esse arquivo de ```views.py```.
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
Ele tem a função de fazer a ponte da ```views.py``` com o ```settings.py``` por maio da constante ```ROOT_URLCONF = 'static.urls'```, em ```settings.py```.

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
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── statics
│   └── css
│       └── skin.css
└── templates
    └── index.html

```

---

# Alteração do settings.py  
[Voltar ao topo(Conteúdo)](#conteúdo)  
As únicas alteração necessária no arquivo ```settings.py``` serão acrescentar ```static``` no final da lista da constante ```INSTALLED_APPS```, conforme abaixo:
 ```py
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # meus app em templates
    'static',
]
```
A constante ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'statics'),]``` no final do arquivo ```settings.py```. E, por fim, preencher a lista `'DIRS': []` em `TEMPLATES` com `os.path.join(BASE_DIR, 'templates')`.  Agora o _Django_ pode achar o arquivo ```html```. Dessa forma indicamos ao _Django_ que temos uma aplicação própria, não padrão. Isso quer dizer que nossa aplicação pode ser compatível com a regra de negócio proposta a partir de um fato concreto. Por padrão, está abilitada a tag especial do _Django_ ```{%  %}``` e o comando ```collectstatics```, ambos, de ```'django.contrib.staticfiles'``` na lista constante ```INSTALLED_APPS```.

Para tornar o arquivo `css` que está em `$ aula3/aula3/statics/css/skin.css` devemos configurar o arquivo `html` e o arquivo `urls.py`.

Até aqui é possível acessar o projeto pronto em  [aula3](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5/aula3) e ver `settings.py`. Antes de acessar o códogo completo, teste seu código e faça a última configuração para dar cor e forma ao seu `app`.

---

# Arquivos estáticos
[Voltar ao topo(Conteúdo)](#conteúdo)  
Observe que o arquivo ```css``` não foi carregado na página ```html``` por meio da linha ```<link rel="stylesheet" href="css/skin.css">```. Para carregar o arquivo da folha de estilo faz-se necessário indicar o arquivo `html` em `$ aula3/aula3/templates/index.html`. Acrescente no topo do arquivo, antes do `<!DOCTYPE html>` a _tag _ do _Django_ `{% load staticfiles %}` e modofique a chamada à folha de estilo externa afim de ter a seguinte sintaxe: `<link rel="stylesheet" href='{% static "css/skin.css" %}' type="text/css" />`. Seu arquivo `index.html` deve estar, no mínimo, conforme abaixo:
```html
{% load staticfiles %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href='{% static "css/skin.css" %}' type="text/css" />
    <title>Index</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```
O últio arquivo a ser alterado é o `urls.py`. Inclua as importações `from django.conf import settings` e `from django.conf.urls.static import static`. É importe destacar que este projeto foi criado sem a prentenção de simular um ambiente de produção. E, sendo assim, a constante `DEBUG` está ativado. O fato de se ter o `DEBUD=True` nos leva o configurar o `urls.py` com um acondição que verifica o estado do `DEBUG` em `settings.py` antes de mudar o `urlpatterns`. O código para isso deverá estar da seghinte forma:
```py
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ola/mundo/$', views.OlaMundo, name='olaMundo'),
    url(r'^status/$', views.status_code, name='status_code'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

Para terminar, execute seu projeto com `$ aulaDjango/py3.5/aula3/manage.py runserver`.

Com isso chega ao fim a oficina para divulgação e apresentação do Framework _Django_1.9 com _Python 3_, que ocorreu no _MundoSenai_ edição 2016.
___


[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
