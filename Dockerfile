FROM python:3.7
RUN mkdir /dockerfile
WORKDIR /dockerfile
COPY requirements.txt /dockerfile
RUN pip install -r requirements.txt 

EXPOSE 1225

COPY . /dockerfile
EXPOSE $PORT
CMD ["uvicorn", "app.main:app","--port", "1225","--bind","0.0.0.0:1225"]