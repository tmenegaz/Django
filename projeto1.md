# Conteúdo

1. **[Primeiro projeto com Django](#primeiro-projeto-com-django)**  

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

No diretório de trabalho para os projetos desse material cie seu Virtualenv e instale seus pacotes
> Neste caso estou no diretório Documentos do Linux: /home/tmenegaz/Documentos/):

Abaixo eu escrevi cada um dos comandos necessários para a configuração do ambiente, a partir do início do Virtualenv até a instalação do Django, sepatados por ponto e vírgula (;).
```sh
$ virtualenv -p python3.5 ./aulaDjnago/py3.5; cd ./aulaDjnago/py3.5/; source aulaDjnago/py3.5/bin/activate; pip3 install -U pip; sudo pip3 install django==1.9; cd ./aulaDjnago/py3.5
```

# O Django
[Voltar ao topo(Conteúdo)](#conteúdo)

Conforme Julia Elman e Mark lavin (Django Essebcial - O'reilly, Novatec), o Django foi originalmente desenvolvido na World Online, em Lawrence, no Kansas - USA, como uma maneira de repórteres criarem conteúdo para a web rapdamente. Apenas para sitar algumas empresas que trabalham com publicação e que usam o Django, desde então:
- The Washington Post;
- The Guardian;

O Django não é um gerenciador de conteúdos. O que colaborou para essa afirmação foi o fato da NASA ter adotado-o como Framework de preferência para atender suas demandas.
O Django é um Framework de alto nível escrito em Python e para ser utilizado com Python, que estimula o desenvolvimento rápido e limpo para a Web. O Framework utiliza um princípio conhecido como **DRY** (Não se repita), Don't Repeat Yourself e utiliza também o padrão de projeto chamado **MVC** (Modelo, Visão e Controle), Model-View-Controller que implica dizer que:
- _modelos_ são para a parte de dados;
- _vizualizações_ são para exibir o conteúdo;
- _controlador_ são para gerir o projeto.

O Django é chamado de _framework MTV_ (Modelo-Template-Visão), Model-Template-View, por ter a parte da _visão_ responsável por inspecionar a solicitação _HTTP_ de entrada e fazer consultas ou composições dos dados importantes que serão enviados a camada de apresentação(_view_).

---

# Instalar o Python em seu SO

## Python no Linux
[Voltar ao topo(Conteúdo)](#conteúdo)

O Python está instalado no Linux. Para saber qual a versão utilizada em sua distribuição Linux abra o terminal  e digite
```sh
$ python -V
python 2.7.12
```
Tente ainda por meio desse comando
```sh
$ python3 -V
python 3.5.2
```
Resultado semelhante pode ser obtido escrevendo python e, em seguida, precionando a tecla _tab_ duas vezes.
```sh
$ python +[2xtab]
python             python2-config     python3.5m         python3m-config
python2            python3            python3.5m-config  python-config
python2.7          python3.5          python3-config     pythontex
python2.7-config   python3.5-config   python3m           pythontex3
```
Para esse material será usada a versão 3 do Python e o Django 1.9. Caso a versão 3 não esteja instalada execute no terminal o camando abaixo para instalar o Python 3.5 e algumas ferramentas de desenvolvimento.
```sh
$ sudo apt update # atualiza os repositórios do seu SO (opcional)
$ sudo apt install python3 idle-python3.5 python3-pip -y
```
---

## Python no Windows
[Voltar ao topo(Conteúdo)](#conteúdo)

O Python não vem instalado no Windows.
Para instalar o Python 3, como única versão no Windows acesse o sítio [python.org/windows](https://www.python.org/downloads/windows/) e baixe o Python 3.5.2 compatível com o seu sistama.
Execute o arquivo, habilite a definição do Path e, em seguida, siga as instruções de instalação. Esse mesmo arquivo de instalação servirá para reparar ou remover o Python 3 do sistema Windiws, caso seja necessário.
Para saber se a instalação com a definição do Path foi bem sucedida e qual a versão utilizada em sua distribuição Windows abra o _cmd_  e digite
```cmd
>py -V
python 3.5.2
```
Pronto, agora você pode usar o Python para instalar o Virtualenv e o django

---

# Instalar o Virtualenv
[Voltar ao topo(Conteúdo)](#conteúdo)

O Virtualenv é uma ferramenta para criar ambientes Python distintos. A vantagem em preparar um ambiente isolado de outro ambiente por meio do Virtualenv é que pode-se criar projetos com versões especificas de programa sem que estes entrem em conflito.
Utilize o pip (índice de pacotes do Python), para instalar o Virtualenv
> Caso o sistema em questão seja o Windows utilize o _cmd_, não escreva _sudo_ antes do comando e, nem tão pouco, o _3_ depois do pip. Ex.:
```cmd
>>pip install virtualenv
```

Para instalar o Virtualenv no Linux use o pip conforme o comando abaixo:
```sh
$ sudo pip3 install virtualenv
```
Para criar seu ambiente com o Virtualenv vá para a pasta que deseja trabalhar e abra-a no terminal. Em seguida execute o comando abaixo:
```sh
$ virtualenv -p python3.5 <nomeDaPasta>
```

> No Windows não precisa digitar _python3.5_ no comando do Virtualenv.

É recomendada a indicação da versão do Python que se deseja utilizar. Para um diretório _meuprojeto_ com um subdiretório _py3.5_. Esse último, indica o a versão do Python que será usada no projeto, neste caso a 3.5.2, ex.:
```sh
$ virtualenv -p python3.5 ./meuprojeto/py3.5
```
Até aqui o Virtualenv está instalado e seu diretório de trabalho pronto. Agora por meio do comando _cd_ vá para o diretório.
```sh
$ cd ./meuprojeto/py3.5/
```
> No Windows use para o  mesmo comando a barra invertida.
```cmd
>>cd .\meuprojeto\py3.5\
```

Caso seja necessário usar as variáveis globais do sistema:
```sh
$ virtualenv -p python3.5 --system-site-packages <nomeDaPasta>
```
Ou, se não for necessário usar as variáveis globais do sistema:
```sh
$ virtualenv -p python3.5 --no-site-packages <nomeDaPasta>
```
Para ativar seu Virtualenv
```sh
$ source <nomeDaPasta>/<nomeDaPasta>/bin/activate
```
Por exemplo: para um pasta meuprojeto/py3.5
```sh
$ source meuprojeto/py3.5/bin/activate
```
> No Windows dentro do diretório que você criou o Virtualenv será criada, dentre outras pastas e arquivos, a pasta _Script_ com o _activate_. Sendo assim invoque o activate:
```cmd
>>meuprojeto/py3.5/Script/activate
```

Para desativar seu Virtualenv
```sh
$ deactivate
```
> No Windows, desative por meio do comando:
```cmd
>>meuprojeto/py3.5/Script/deactivate
```

Para remover seu Virtualenv
```sh
$ revirtualenv <nomeDaPasta>
```
> No Windows, remova por meio do comando:
```cmd
>>revirtualenv <nomeDaPasta>
```

Agora, caso tenah desativado o Virtualenv inicie-o para instalar o Django e criar seu primeiro projeto.

# Instalar o Django
[Voltar ao topo(Conteúdo)](#conteúdo)

Uma vez instalado o Python 3, o pip e o Virtualenv é hora de instalar o Django. Para começar a utilizar o Django digite o comando abaixo, no terminal, por meio do pip, em seu Virtualenv:
```sh
$ pip3 install -U pip # atualiza o pip3 (recomendado)
$ sudo pip3 install django==1.9
```
> Lembre-se, no Windos não utilize o _3_ depois do _pip_ e nem a palavra _sudo__.
```cmd
>>pip install -U pip # atualiza o pip
>>pip install django==1.9
```

Uma dica: o pip3 permite fazer uma lista dos potes que estão em um certo computador para, posteriormente, isntalá-los em outro computador:

```sh
$ pip3 freeze > requeriments.txt
```
Instalar os requisitos e dependência no outro computador
```sh
$ pip3 install -r requeriments.txt
```
Agora é possível criar um primeiro projeto com o Django.

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
