FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
#COPY entrypoint.sh ./entrypoint.sh
#RUN chmod +x ./entrypoint.sh

#ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
