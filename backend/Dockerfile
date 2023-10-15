FROM python:3.9
WORKDIR app/
RUN pip install gunicorn==20.1.0
COPY requirements.txt requirements.txt
COPY backend .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "--bind", "0:9006", "backend.wsgi"]