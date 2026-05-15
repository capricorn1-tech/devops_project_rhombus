FROM python:3.11-alpine

WORKDIR /app

COPY app.py .

COPY docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3","app.py"]
