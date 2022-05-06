FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /testando/

COPY . /testando/
RUN pip install -r ./requirements.txt 


EXPOSE 5000
CMD ["python", "do.py"]
