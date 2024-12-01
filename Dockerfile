FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["bash", "-c", "python -m unittest discover -s ./tests  -p 'test_*.py'"]
