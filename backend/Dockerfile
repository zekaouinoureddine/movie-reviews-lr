FROM python:3.9.5
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir -r /code/requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]