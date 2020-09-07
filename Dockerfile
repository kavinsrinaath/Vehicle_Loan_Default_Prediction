FROM python:3.7
RUN mkdir /dockerfile
WORKDIR /dockerfile
COPY requirements.txt /dockerfile
RUN pip install -r requirements.txt 

EXPOSE 80

COPY . /dockerfile

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]