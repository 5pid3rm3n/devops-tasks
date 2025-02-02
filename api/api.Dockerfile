FROM python:3.9

WORKDIR /code

# Copy requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code
COPY . /code/api

# Run the FastAPI application
CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "3000"]