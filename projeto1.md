# Conteúdo

1. **[Primeiro projeto com Django](#primeiro-projeto-com-django)**  
1.1 [Comandos de ativação do ambiente](#comandos-de-ativação-do-ambiente)  
2. **[O projeto](#o-projeto)**  
2.1 [Aula1](#aula1)  

---

# Primeiro projeto com Django
[Voltar ao topo(Conteúdo)](#conteúdo)   
Para esse projeto, e os demais, o ambiente de desenvolvimento Python/Django possui as segintes configurações básicas, a saber:
- Linux - Ubuntu 16.04;
- Python 3;
- pip3;
- Virtualenv;
- Django 1.9;
- Atom (editor de texto)
- Plugins do  Atom (referencia: Cruz, Renato dos Santos - Iniciando no Django 1.9)
    - Highlight Selected;
    - Linter-pep8;
    - atom-beautify;
    - atom-jango;
    - python-tools.

## Comandos de ativação do ambiente
[Voltar ao topo(Conteúdo)](#conteúdo)   
No diretório de trabalho para os projetos desse material crie seu Virtualenv e instale suas bibliotecas.
> Neste caso, estou no diretório Documentos do Linux: /home/tmenegaz/Documentos/)

Abaixo estão, reunidos em apenas uma linha, cada um dos comandos necessários para a configuração do ambiente, a partir do carregamento do Virtualenv até a instalação do Django, sepatados por &&.
Abra seu _terminal_ Linux com ```Ctrl+Alt+t```.
```sh
$ virtualenv -p python3.5 ./aulaDjango/py3.5 && cd ./aulaDjango/py3.5/ && source ./bin/activate && pip3 install -U pip && pip3 install django==1.9
```

> No windows, abra o _cmd_ com ```Winkey(simbolo windows)+r``` digite _cmd_, precione ```Enter``` e, então, use o comando abaixo.
```cmd
>>virtualenv .\aulaDjango\py3.5 && cd .\aulaDjango\py3.5\ && .\Scripts\activate.bat && pip install -U pip && pip install django==1.9
```

Serão incorporados ao ambiente de desenvolvimento novos itens, na medida em que o projeto necessite da instalação de alguma nova biblioteca ou ferramenta.

---

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)  
Caso o Virtualenv não esteja ativado, ative-o: pelo _terminal_ do Linux, em seu diretório ```py3.5$``` ative o virtualenv,  por meio do comando
```sh
py3.5$ source ./bin/activate
(py3.5)tmenegaz@tam:~/Documentos/aulaDjango/py3.5$
```
Em seguida digite ```pip3 list``` para saber se o django está devidamente instalado na versão 1.9 do seu virtualenv.
```sh
py3.5$ pip3 list
Django (1.9)
pip (8.1.2)
setuptools (28.3.0)
wheel (0.30.0a0)
```
Caso não esteja conforme acima volte para [Comandos de ativação do ambiente](#comandos-de-ativação-do-ambiente)  e refaça o processo.

---

## Aula1
[Voltar ao topo(Conteúdo)](#conteúdo)  
Esse primeiro projeto terá o nome _aula1_ e um conjunto de pastas e arquivos gerados automaticamente pelo Django. Em seu diretório ```py3.5$``` digite o comando abaixo para criar seu projeto Django.
```sh
py3.5$ django-admin startproject aula1
```
> No _cmd_ do Windows digite
```cmd
py3.5>django-admin startproject aula1
```

O projeto pode ser testado em seu ```web browser```. Para isso, acesse por meio do _terminal_ seu diretório _aula1_ e digite o camando abaixo.
```sh
aula1$ ./manage.py runserver
```
> No _cmd_ do Windows digite
```cmd
aula1>.\manage.py runserver
```

O comando acima carregou o projeto _aula1_ para o servidor interno do Django. Agora acesse em seu ```web browser``` a _url_ [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver a mensagem _It worked!_

Agora é chegada a hora de entender o que o comando ```django-admin startproject aula1``` gerou e para que serve cada pasta e arquivo criada. Por meio da barra de ferramentas do ```Atom```: ```File/Open Folder``` selecione a pasta ```aula1``` e clique em ```ok```.

---

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
