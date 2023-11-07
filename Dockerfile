FROM python:3.11.0-alpine
WORKDIR /code
EXPOSE 8000
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
