FROM python:3.9

WORKDIR /app

COPY src .

CMD ["python3", "reverse-shell.py"]
