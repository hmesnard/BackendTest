FROM python:3

RUN git clone https://github.com/HuMoran/aapt

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 manage.py runserver 0.0.0.0:8000
