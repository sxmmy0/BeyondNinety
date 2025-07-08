FROM python:3.11-slim

WORKDIR /code

COPY ./byd90/app /code/app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]