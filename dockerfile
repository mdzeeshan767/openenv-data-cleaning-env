FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# 👇 IMPORTANT: keep container alive + run script
CMD python scripts/run_baseline.py