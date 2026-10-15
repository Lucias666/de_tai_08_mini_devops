import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # Lấy thông tin kết nối từ Biến môi trường (Mặc định sẽ dùng các giá trị vế sau nếu không tìm thấy)
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '5432')
    db_name = os.environ.get('DB_NAME', 'devops_db')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_pass = os.environ.get('DB_PASS', 'postgres')
    
    db_status = "Disconnected"
    error_msg = None
    
    # Thử kết nối tới PostgreSQL
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        db_status = "Connected to PostgreSQL successfully!"
        conn.close()
    except Exception as e:
        # Bắt lỗi để sau này dễ Troubleshooting khi giảng viên đánh sập Database
        error_msg = str(e)
    
    # Trả về kết quả dạng JSON
    return jsonify({
        "project": "Mini DevOps Environment",
        "message": "Hello from Flask Web App!",
        "database_status": db_status,
        "error": error_msg
    })

if __name__ == '__main__':
    # Chạy app ở port 5000, host 0.0.0.0 là bắt buộc để Docker có thể map port ra bên ngoài container
    app.run(host='0.0.0.0', port=5000)
