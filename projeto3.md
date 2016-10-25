# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1. [Aula3](#aula3)  
1.2. [Alteração do settings.py](#alteração-do-settingspy)  
1.3. [Arquivos estáticos](#arquivos-estáticos)

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Evidentemente que você notou o comando ```python manage.py startapp [app_label]``` quando rodou o seu projeto aula1 ou testou aula2 e aula3, após executar o comando ```manage.py runserver``` pela primeira vez, em cada projeto. Esse comando cria para seu projeto os diretórios e arquivos necessários para sua aplicação. Ainda não será utilizada a linha de código acima. Entende-se ser razoável a criação de uma estrutura sem comandos para proporcionar um melhor entendimento da arquitetura do _Django_ nos projetos. Aqui será criado um modelo semelhante ao do comando para dar condições de preservar a modularização parcial do projeto. Serão criados diretórios e arquivos com a disposições específicas.
```sh
  aula3
│   ├── templates
│   │   └── aula3
│   │       ├── css
│   │       │   └── skyn.css
│   │       └── index.html
```
Para cada um dos arquivos, crie elementos básiicos para testar sua aplicação. No arquiivo ```skyn.css``` foram digitadas as seguintes linhas:
 ```css
 @charset "UTF-8";

body {
    background-color: #000;
}

h1 {
    color: #fff;
}
 ```
No arquivo ```index.html``` tem-se as seguintes linhas:
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
  
---

## Aula3
[Voltar ao topo(Conteúdo)](#conteúdo)  
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
Para cada um dos arquivos, crie elementos básiicos para testar sua aplicação. No arquiivo ```skyn.css``` foram digitadas as seguintes linhas:
 ```css
 @charset "UTF-8";

body {
    background-color: #000;
}

h1 {
    color: #fff;
}
 ```
No arquivo ```index.html``` tem-se as seguintes linhas:
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
Em ```$ aula3/aula3/``` crie  seu arquivo ```views.py``` com o seginte código:
```py

```
Após criar os diretórios e arquivos o seu projeto terá a seguinte disposição:
```
from django.shortcuts import render
from django.http import HttpResponse

# criar a view
def index(request):
    return render(request,'aula3/index.html',{})

def OlaMundo(request):
    return HttpResponse("Olá mundo!")

def status_code(request):
    return HttpResponse("Resposta %s" % (HttpResponse.status_code))
```

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

---

# Arquivos estáticos
[Voltar ao topo(Conteúdo)](#conteúdo)  

---

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
