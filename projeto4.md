# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1. [Aula4](#aula4)  

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Por meio do _terminal_ do Linux, em seu diretório ```py3.5$```, siga os seguintes passos:

- ative o _virtualenv_:

```sh
py3.5$ source ./bin/activate
(py3.5)tmenegaz@tam:~/Documentos/aulaDjango/py3.5$
```

> Caso existam dúvudas, ainda, quanto a ativação e criação do projetos consulte o material do _projeto_ em [_aula2_](https://github.com/tmenegaz/django/blob/master/projeto2.md#o-projeto).

- Crie seu novo projeto Django:
    
```sh
py3.5$ django-admin startproject aula4
```

- Crie sua app

```sh
/py3.5/aula4$ ./manage.py startapp app
```

A partir das instruções executadas você teré um conjunto de diretórios e arquivos organizados da seguinte forma:
```sh
../aula4
├── app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── aula4
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```


---------

## Aula4
[Voltar ao topo(Conteúdo)](#conteúdo)  

___


[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
