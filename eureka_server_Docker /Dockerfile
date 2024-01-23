# Dockerfile


FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./eureka-server.py /app/main.py

EXPOSE 8761

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8761"]