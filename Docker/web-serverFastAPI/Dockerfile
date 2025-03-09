FROM python:3.13

WORKDIR /web-serverFastAPI
COPY requeriments.txt /web-serverFastAPI/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /web-serverFastAPI/requeriments.txt

COPY . /web-serverFastAPI/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8043"]