# Đề tài 08: Dockerized Mini DevOps Environment

## 1. Giới thiệu dự án
Dự án giả lập môi trường phát triển (Development Environment) với kiến trúc Microservices cơ bản, quản lý hoàn toàn bằng Docker Compose.

**Kiến trúc hệ thống:**
`Người dùng` ➔ `Nginx (Port 80)` ➔ `Flask Web App (Port 5000)` ➔ `PostgreSQL (Port 5432)`

## 2. Cấu trúc thư mục
- `/web`: Chứa mã nguồn Python/Flask và Dockerfile.
- `/nginx`: Chứa cấu hình Reverse Proxy.
- `compose.yaml`: File định nghĩa hạ tầng (Infrastructure as Code).
- `.env.example`: Chứa file mẫu khai báo biến môi trường.

## 3. Hướng dẫn vận hành (Lifecycle Management)

Dự án này sử dụng Docker Compose để quản lý toàn bộ vòng đời của hệ thống. Dưới đây là các lệnh thao tác cơ bản:

**1. Khởi tạo và xây dựng hệ thống:**
```bash
# Build image cho Web App
docker compose build

# Khởi động toàn bộ hệ thống chạy ngầm (Detached mode)
docker compose up -d
