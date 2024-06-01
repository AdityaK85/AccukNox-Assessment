From python:3.12.1

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000