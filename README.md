# PROJETO TESTE USANDO FLASK

## Descrição:
Esse arquivo contem uma página contruida com o framework flask, existe uma pagína base e páginas que podem ser navegadas via barra de naveação. Na página login há um formulário de autenticação que o flask roda a resposta após a sumbmissão do formulário.
Esse projeto além de usar o flask utiliza o docker com o arquivo Dockerfile criando uma imagem da página de navegação e de todos os requerimentos para executar a página.
Para construir o arquivo o docker no Powershell da IDE precisa rodar o seguinte código:
 - docker build -t nomeprojeto .
 Para rodar diretamente a imagem usando docker:
 - docker run -d -p 5000:5000 nomeprojeto

 ### Arquivo principal:
 do.py
 ### Arquivos secundários:
 /static/
 /templates/
 requirements.txt
 Dockerfile

 ### Arquivo opcionais:
 .flaskenv: permite usar o docker em modo de produção
 Procfile: cria interligação com o heroku






