# Conteúdo

1. **[Primeiro projeto com Django](#primeiro-projeto-com-django)**  
2. **[O projeto](#o-projeto)**  

---

# Primeiro projeto com Django
[Voltar ao topo(Conteúdo)](#conteúdo)

Para esse projeto e os demais ambiente de desenvolvimento Python/Django tenha em mente as segintes características, a saber:
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

No diretório de trabalho para os projetos desse material crie seu Virtualenv e instale seus pacotes
> Neste caso estou no diretório Documentos do Linux: /home/tmenegaz/Documentos/)

Abaixo está escritp em uma linha cada um dos comandos necessários para a configuração do ambiente, a partir do carregamento do Virtualenv até a instalação do Django, sepatados por &&.
```sh
$ virtualenv -p python3.5 ./aulaDjango/py3.5 && cd ./aulaDjango/py3.5/ && source ./bin/activate && pip3 install -U pip && sudo pip3 install django==1.9
```
> No windows use o comando abaixo:
```cmd
>>virtualenv .\aulaDjango\py3.5 && cd .\aulaDjango\py3.5\ && .\Scripts\activate.bat && pip install -U pip && pip install django==1.9
```

# O projeto
[Voltar ao topo(Conteúdo)](#conteúdo)

"A definir"

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
