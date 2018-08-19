FROM python:3.7-stretch

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y netcat
RUN pip install --no-cache-dir -r requirements.txt

ADD https://raw.githubusercontent.com/eficode/wait-for/master/wait-for /bin/wait-for
RUN chmod a+rx /bin/wait-for

COPY iptest.py .
CMD [ "/bin/wait-for", "ip:80", "--",  "python", "./iptest.py"]
