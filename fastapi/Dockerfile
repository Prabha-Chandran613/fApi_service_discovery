FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]























# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# RUN mkdir -p /app

# WORKDIR /app
 
# # Copy the requirements file into the container at /app
# COPY requirements.txt .
 
# # Install any needed packages specified in requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir sqlalchemy psycopg2-binary
 
# # Copy the current directory contents into the container at /app
# COPY . .
 
# # Expose port 80 for the FastAPI application
# EXPOSE 8001
 
# # Command to run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
