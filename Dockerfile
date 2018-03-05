FROM alpine:3.1

#Update
RUN apk add --update python py-pip

#Bundle app source

COPY runner.py /src/runner.py

EXPOSE 8000

CMD ["python","/src/runner.py","-p 8000"]

