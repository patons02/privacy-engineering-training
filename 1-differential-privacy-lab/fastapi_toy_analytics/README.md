# 🛡️ FastAPI Toy Analytics Platform — Local Differential Privacy

Built by **patons02**

---

## 📖 Overview

This project demonstrates a live toy analytics platform where:
- Users simulate interactions (clicks, typing)
- Local Differential Privacy (Randomized Response) is applied immediately on the client-side
- Noised data is sent to the server (FastAPI)
- Server aggregates noised data and estimates true counts

---

## 📚 How It Works

1. **Frontend (Static Site):**
   - User clicks buttons to simulate actions
   - Each action is noised (locally) using randomized response
   - Sends noised event to backend via AJAX POST

2. **Backend (FastAPI Server):**
   - Receives noised events
   - Aggregates incoming events
   - Provides estimated true counts via REST API

---

## ⚙️ Setup

Install dependencies:

```bash
pip install fastapi uvicorn numpy
```

Run the server:

```bash
uvicorn app.main:app --reload
```

Open your browser at:

```bash
http://127.0.0.1:8000/static/index.html
```

Start clicking!

---

## 📜 License

Restricted License:

- No resale, no rebranding without written permission.
- No reproduction of certificates without author signature.
- Educational and personal portfolio use only.

---

## 🚀 Build privacy-first systems!
