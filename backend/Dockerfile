FROM python:3.9
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "--bind", "0:9006", "backend.wsgi", "--reload"]