FROM python:3

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD python3 manage.py runserver 0.0.0.0:8000
