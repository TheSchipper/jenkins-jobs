FROM python:3.10-slim

# Copy workspace
WORKDIR /workspace
COPY . /workspace

RUN apt-get update

RUN pip install --index-url http://172.26.34.58:8000/simple/ -r requirements.txt

ENTRYPOINT ["python", "main.py"]