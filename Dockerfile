FROM python:3.10

WORKDIR /app/

COPY ./requirements.txt /app/
ADD src /app/src
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "src"]
