FROM python:3.9-slim

WORKDIR /weatherapp

COPY weather_severity.py .
COPY test_weather_severity.py .

RUN pip install pytest

CMD ["python", "weather_severity.py"]