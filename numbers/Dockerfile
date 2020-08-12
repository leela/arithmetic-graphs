FROM python:3.7

WORKDIR /numbers

EXPOSE 80

COPY . /numbers

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
