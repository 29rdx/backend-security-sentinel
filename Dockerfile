FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt* ./
RUN pip install --no-cache-dir requests cryptography pyjwt rich pytest

COPY . .
RUN pip install --no-cache-dir -e .

ENTRYPOINT ["backend-sentinel"]
CMD ["--help"]
