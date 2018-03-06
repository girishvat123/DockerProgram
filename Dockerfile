FROM alpine:3.1
FROM python:3
#Update
RUN apk add --update python py-pip

#Bundle app source

COPY runnable.py /src/runnable.py

EXPOSE 8000

CMD ["python","/src/runnable.py","-p 8000"]

