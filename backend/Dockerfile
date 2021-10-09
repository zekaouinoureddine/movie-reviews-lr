FROM python:3.9.5
WORKDIR /code
COPY . /code
RUN pip install pip==21.2.4
RUN pip install --no-cache-dir -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]