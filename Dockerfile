FROM alpine:3.1

#Update
RUN apk add --update python py-pip

#Bundle app source

COPY runnable.py /src/runnable.py

EXPOSE 8000

CMD ["python3","/src/runnable.py","-p 8000"]

