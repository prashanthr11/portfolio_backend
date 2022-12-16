FROM python:3.11.1-slim-buster


COPY . /src/api/
WORKDIR /src/api/
RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
