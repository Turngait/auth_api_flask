FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update
RUN apt-get install python3-mysqldb -y
RUN pip install mysqlclient python-dotenv Flask flask-sqlalchemy Werkzeug
RUN pip install -U flask-cors
RUN pip install PyMySQL
RUN pip install requests
WORKDIR /api
COPY api /api

CMD ["python", "main.py"]