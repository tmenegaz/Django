# Conteúdo

1. **[O projeto](#o-projeto)**  
1.1 [Aula2](#aula2)  

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

Se quiser teste seu projeto da mesma forma que fez anteriormente, corregue-o no _browser_ por meio do comando ```./manage.py runserver```. Tudo funciona bem!

Por meio da barra de ferramentas do ```Atom```: ```File/Open Folder``` selecione a pasta ```aula2``` e clique em ```ok```.

O projeto [_aula2_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5) tema mesma estrutura do projeto [_aula1_](https://github.com/tmenegaz/django/tree/master/aulaDjango/py3.5). O que faremos é aproveitar essa estrutura para crir a nossa própria _view_ e indicar o caminho pela _urls_ para que o _browser_ encontre o conteúdo da _view_. Nesse caso testaremos se o _navegador_ retorna na tela a frase **Hello World!**. Esse processo será, em um primeiro momento, construido sem a modularização ofericida como padrão pela instrução ```django-admin```. Aqui, nesse momento, aglutina-se a _view_ no arquivo _settings.py_. O que se quer com isso é mostrar a grande capacidade de acoplamento do Python para trechos de códigos que podem ser reunidos em um arquivo ou em arquivos distintos. Isso é possível, em _Python_, sem demandar esforços para além da _sintaxe_ da Linguagem. 

---

[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License](http://creativecommons.org/licenses/by/3.0/)
