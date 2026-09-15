FROM python:3.12-slim

WORKDIR /app

COPY deployment/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY deployment/app.py .

EXPOSE 5000

CMD ["python", "app.py"]
