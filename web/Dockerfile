FROM python:3.12-alpine
WORKDIR /app
RUN adduser -D appuser
COPY requirements.txt .
RUN apk update && apk add --no-cache postgresql-libs gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
