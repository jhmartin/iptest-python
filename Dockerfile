FROM python:3.7-stretch

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY iptest.py .
CMD [ "python", "./iptest.py"]
