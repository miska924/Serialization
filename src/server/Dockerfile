FROM python:3.10

EXPOSE 2919
EXPOSE 2920
EXPOSE 2921
EXPOSE 2922
EXPOSE 2923
EXPOSE 2924

WORKDIR /app/

COPY requirements.txt /app/
ADD src /app/src
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "src.server"]
