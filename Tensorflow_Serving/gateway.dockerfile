FROM python:3.12.11-slim
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY ["requirements.txt", "./"]
RUN pip install --no-cache-dir -r requirements.txt
COPY ["gateway.py","./"]
EXPOSE 9600
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9600","gateway:app"]