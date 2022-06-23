FROM python:3.9.13

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    pip install requests && \
    rm requirements.txt

COPY main.py main.py

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1" ]
