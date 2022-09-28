FROM python:3.9
WORKDIR /colored_logger

COPY . /colored_logger
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
