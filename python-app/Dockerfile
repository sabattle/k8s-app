FROM python:3

WORKDIR /usr/src/app/

COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
