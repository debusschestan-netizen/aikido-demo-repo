FROM python:3.8-slim

ARG DEMO_SECRET=demosecret123
ENV DEMO_SECRET=${DEMO_SECRET}

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
