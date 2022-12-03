FROM alpine:3.14
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN apk --no-cache add firefox

COPY ripper/ ripper
WORKDIR "/ripper"
RUN "ls"

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "overleaf-ripper.py"]