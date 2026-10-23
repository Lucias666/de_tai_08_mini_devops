
import os
from contextlib import closing

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def hello():
    try:
        with closing(
            psycopg2.connect(
                host=os.environ["DB_HOST"],
                port=int(os.environ.get("DB_PORT", "5432")),
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASS"],
                connect_timeout=3,
            )
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()

        return jsonify({
            "project": "Mini DevOps Environment",
            "message": "Hello from Flask Web App!",
            "database_status": "Connected",
            "error": None,
        }), 200

    except (psycopg2.Error, KeyError, ValueError):
        app.logger.exception("Database connection check failed")

        return jsonify({
            "project": "Mini DevOps Environment",
            "message": "Database is unavailable",
            "database_status": "Disconnected",
            "error": "Database connection failed",
        }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
