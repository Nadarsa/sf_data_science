FROM python:3.9
WORKDIR /usr/scr/app
COPY ./app ./
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./server.py"]