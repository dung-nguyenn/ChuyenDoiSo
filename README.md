<div align="center">
  <p align="center">
    <img src="https://raw.githubusercontent.com/anhminhvdvn/CanhBaoDotNhap/main/images/logoDaiNam.png" width="150"> </p> <br>




</br> </div>

# 💆‍♀️ Spa AI Booking Agent

### *Trợ Lý AI Đặt Lịch Spa Tự Động*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge\&logo=google\&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-121212?style=for-the-badge\&logo=chainlink\&logoColor=white)](https://www.langchain.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People%20with%20Activities/Woman%20in%20Steamy%20Room.png" alt="Spa Icon" width="150" />

**Ứng dụng đặt lịch Spa thông minh bằng AI — lưu trữ, kiểm tra và quản lý lịch hẹn tự động.**

[🚀 Demo](#-demo) • [✨ Tính Năng](#-tính-năng) • [📦 Cài Đặt](#-cài-đặt) • [💬 Sử Dụng](#-sử-dụng) • [📖 Tài Liệu](#-tài-liệu) • [🤝 Đóng Góp](#-đóng-góp)

---

</div>

## 📋 Mục Lục

* [Giới Thiệu](#-giới-thiệu)
* [Tính Năng](#-tính-năng)
* [Công Nghệ](#-công-nghệ)
* [Kiến Trúc Hệ Thống](#-kiến-trúc-hệ-thống)
* [Cài Đặt](#-cài-đặt)
* [Sử Dụng](#-sử-dụng)
* [Tài Liệu](#-tài-liệu)
* [Screenshots](#-screenshots)
* [Roadmap](#-roadmap)
* [Đóng Góp](#-đóng-góp)
* [License](#-license)

---

## 🎯 Giới Thiệu

**Spa AI Booking Agent** là ứng dụng web thông minh giúp khách hàng **đặt lịch hẹn spa tự động** bằng cách trò chuyện trực tiếp với **AI Agent**.
Dự án sử dụng **Google Gemini 2.5 Flash**, **LangChain** và **Streamlit** để mang lại trải nghiệm tự nhiên, nhanh chóng và thân thiện.

### 🌟 Điểm Nổi Bật

* 🤖 **Trợ lý AI thân thiện** — tương tác tự nhiên bằng tiếng Việt
* 💅 **Đặt lịch tự động** — nhập tên, chọn dịch vụ, chọn thời gian
* 💾 **Lưu lịch hẹn vào SQLite Database**
* 🔍 **Kiểm tra lịch hẹn trùng** — tránh xung đột thời gian
* 🧾 **Danh sách dịch vụ rõ ràng** — tên, giá và thời lượng
* 📋 **Hiển thị lịch đã đặt ở sidebar**

---

## ✨ Tính Năng

### 🧠 1. Chatbot AI Đặt Lịch

* Người dùng nhập yêu cầu (ví dụ: “Tôi muốn đặt lịch massage body lúc 14h mai”)
* AI tự động hiểu yêu cầu, hỏi thêm thông tin còn thiếu
* Khi đủ dữ liệu → đặt lịch và lưu vào cơ sở dữ liệu

### 🧖‍♀️ 2. Liệt Kê Dịch Vụ

* Xem danh sách tất cả dịch vụ spa hiện có:

  * Massage Body – 90 phút – 750.000 VND
  * Chăm Sóc Da Mặt Cơ Bản – 60 phút – 500.000 VND
  * Tắm Trắng – 120 phút – 1.500.000 VND

### 🗓️ 3. Quản Lý Lịch Hẹn

* Xem tất cả lịch hẹn đã đặt trong **sidebar**
* Lưu lịch hẹn vào **SQLite database**
* Kiểm tra trùng lịch tự động

### 🧱 4. Tích Hợp LLM (Gemini AI)

* Sử dụng **Gemini 2.5 Flash** thông qua `langchain_google_genai`
* Tích hợp qua API key an toàn bằng biến môi trường

---

## 🛠️ Công Nghệ

| Thành Phần                                                                                                 | Phiên Bản | Mục Đích           |
| ---------------------------------------------------------------------------------------------------------- | --------- | ------------------ |
| ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python\&logoColor=white)                   | 3.10+     | Ngôn ngữ chính     |
| ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-FF4B4B?logo=streamlit\&logoColor=white)         | Latest    | Giao diện web      |
| ![LangChain](https://img.shields.io/badge/LangChain-Latest-121212?logo=chainlink\&logoColor=white)         | Latest    | Quản lý công cụ AI |
| ![Google Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-Latest-8E75B2?logo=google\&logoColor=white) | 2.5 Flash | Mô hình ngôn ngữ   |
| ![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite\&logoColor=white)                     | 3.x       | Lưu trữ lịch hẹn   |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Latest-FF6F00?logo=database\&logoColor=white)        | Latest    | ORM cho SQLite     |
| ![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?logo=pydantic\&logoColor=white)                | V2        | Validate dữ liệu   |

---

## 🧩 Kiến Trúc Hệ Thống

```
┌───────────────────────────────────────────────┐
│                   FRONTEND                    │
│             (Streamlit Chat UI)               │
│   ┌──────────────────────────────────────┐    │
│   │  Giao diện chat & sidebar lịch hẹn   │    │
│   └──────────────────────────────────────┘    │
└────────────────────────────┬──────────────────┘
                             │
┌────────────────────────────▼──────────────────┐
│                LANGCHAIN AGENT                │
│  • ChatGoogleGenerativeAI (Gemini 2.5 Flash) │
│  • Tools: list, book, check appointments     │
└────────────────────────────┬──────────────────┘
                             │
┌────────────────────────────▼──────────────────┐
│                 DATABASE LAYER                │
│          SQLite + SQLAlchemy ORM              │
│  • appointments.db                            │
│  • CRUD lịch hẹn                              │
└───────────────────────────────────────────────┘
```

---

## 📦 Cài Đặt

### Yêu Cầu

* Python 3.10 trở lên
* Cài đặt `pip`
* Kết nối Internet (để gọi Gemini API)

### 1️⃣ Clone Project

```bash
git clone https://github.com/<your-username>/spa-ai-booking-agent.git
cd spa-ai-booking-agent
```

### 2️⃣ Tạo Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```

### 3️⃣ Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Thiết Lập API Key

Tạo biến môi trường trong terminal:

```bash
# Windows PowerShell
$env:GEMINI_API_KEY="YOUR_API_KEY"

# Linux / macOS
export GEMINI_API_KEY="YOUR_API_KEY"
```

> 🔑 Lấy API Key tại: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 5️⃣ Chạy Ứng Dụng

```bash
streamlit run app.py
```

---

## 🚀 Sử Dụng

1️⃣ Mở ứng dụng tại [http://localhost:8501](http://localhost:8501)
2️⃣ Chat với AI — ví dụ:

> “Tôi muốn đặt lịch massage body lúc 15h ngày 25/12 cho Linh.”
> 3️⃣ Xem lịch đã đặt trong **sidebar**
> 4️⃣ AI sẽ lưu và hiển thị lịch hẹn từ database

---

## 🖼️ Screenshots

| Chatbot                                       | Sidebar Lịch Hẹn                            |
| --------------------------------------------- | ------------------------------------------- |
| ![Chat Demo](https://i.imgur.com/MrwGqL8.png) | ![Sidebar](https://i.imgur.com/RmVYj8U.png) |

---

## 🧾 Roadmap

* [x] Chatbot AI đặt lịch spa
* [x] Lưu lịch vào SQLite
* [ ] Xóa / cập nhật lịch hẹn
* [ ] Gợi ý dịch vụ phù hợp với khách hàng
* [ ] Gửi email xác nhận lịch
* [ ] Tích hợp API lịch Google Calendar

---

## 🤝 Đóng Góp

1️⃣ Fork repo
2️⃣ Tạo nhánh mới:

```bash
git checkout -b feature/new-feature
```

3️⃣ Commit thay đổi:

```bash
git commit -m "Add new feature"
```

4️⃣ Push và mở Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 👩‍💻 Tác Giả

**Nguyễn Dung**

* 📍 Nam Định, Việt Nam
* 📧 Email: dn427680@gmail.com (liên hệ cá nhân)
* 🧠 Dự án thực tập tại **Công ty Công Nghệ Thương Mại VNA MADE**

---

<div align="center">

**⭐ Nếu bạn thấy dự án này hữu ích, hãy cho một star nhé! ⭐**

Made with 💖 by [Nguyễn Dung](https://github.com/)

</div>

