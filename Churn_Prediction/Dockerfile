FROM python:3.12.11-slim
WORKDIR /app
COPY ["requirements.txt","Pipfile","Pipfile.lock", "./"]
RUN pip install --no-cache-dir -r requirements.txt
COPY ["query.py","Churn_Prediction_model_C=1.bin","./"]
EXPOSE 9601
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9601","query:app"]