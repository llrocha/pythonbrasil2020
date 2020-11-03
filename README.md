# Descrição

Se você está disposto a ler esse documento, parabéns, acho que você vai aprender algumaa coisa.
Em primeiro lugar o ambiente de desenvolvimento, eu deixei na raíz do projeto, um arquivo chamado Pipfile, ele é para ser usado com o pipenv.

A base de CEP que foi usada, você pode encontrar em: http://cep.la/CEP-dados-2018-UTF8.zip
Existem mais duas bases, eu não sei se elas tem o mesmo formato que essa, portanto pode ser que o programa que constrói a base de CEPs, quebre, caso não esteja no layout da base indicada.

Para iniciar seu ambiente de testes e desenvolvimento execute:
```
$ pipenv shell
```

Para rodar o programa, você vai primeiro precisar da base de CEPs, para isso execute:
```
python build_database.py
```

Agora sim, com a base de CEPs construida, você pode começar a executar o nosso microsserviço:
```
python main.py
```

Agora para poder testar, abra http://localhost:8080/



