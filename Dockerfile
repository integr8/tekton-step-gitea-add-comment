FROM python:3-alpine
LABEL maintainer="Fábio Luciano <fabio@naoimporta.com>"
WORKDIR /app

ADD entrypoint.py /usr/local/bin/
ADD requirements.txt /app

RUN pip install -r requirements.txt \ 
  && chmod +x /usr/local/bin/entrypoint.py
USER 1000

ENTRYPOINT ["python3", "/usr/local/bin/entrypoint.py" ]