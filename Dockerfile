#o arquivo parte de tiangolo usando flask
FROM tiangolo/uwsgi-nginx-flask:python3.8

#crio o diretorio do meu app
WORKDIR /testando/

#copio os arquivo necessarios para rodar e rodo a instalção de requerimentos
COPY do.py requirements.txt /testando/
#copiando as pastas templates e stattic para subpastas do app
COPY  /templates/ /testando/templates/
COPY /static/ /testando/static/ 
RUN pip install -r ./requirements.txt 

#exponho a porta
EXPOSE 5000
#peço para rodar o arquivo
CMD ["python", "do.py"]
