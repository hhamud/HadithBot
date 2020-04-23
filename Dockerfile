
FROM python:latest



COPY requirements.txt .
RUN pip install -r requirements.txt



COPY . .


CMD exec gunicorn --bind 0.0.0.0:8000 app:app







