FROM python:3.9-slim

WORKDIR /weatherapp

COPY weather_severity.py .

ENTRYPOINT ["python", "weather_severity.py"]
