FROM python:3.9

#
WORKDIR /code


COPY requirements.txt ./

#
RUN pip install --no-cache-dir -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






















# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# RUN mkdir -p /app

# WORKDIR /app
 
# # Copy the requirements file into the container at /app
# COPY requirements.txt .
 
# # Install any needed packages specified in requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
 
# # Copy the current directory contents into the container at /app
# COPY . .
 
# # Expose port 80 for the FastAPI application
# EXPOSE 8000
 
# # Command to run the application
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]










# # Set working directory inside the container
# WORKDIR /app

# # Copy the entire contents of your Microservice 1 project into the container
# COPY . .

# # Install any dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose the port your FastAPI application is running on
# EXPOSE 8002

# # Command to run the FastAPI application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
