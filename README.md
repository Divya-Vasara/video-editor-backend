# 🎬 Video Editing Backend (Python - FastAPI)

A scalable backend service for uploading, editing, rendering, and downloading videos. Built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **FFmpeg**.

---

## 🧰 Tech Stack

- **FastAPI** - High-performance Python web framework
- **SQLAlchemy** - ORM for PostgreSQL
- **FFmpeg** - Video processing (trimming, subtitles, rendering)
- **Uvicorn** - ASGI web server
- **Pydantic** - Schema validation
- **dotenv** - Environment config
- **python-multipart** - File uploads

---

## 🚀 Features

- ✅ Upload video (any format)
- ✂️ Trim video (start and end timestamp)
- 💬 Add subtitles (with time range)
- 🧪 Render final video (combine edits)
- 📥 Download final rendered video

---

## 🛠 Installation

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/video-editor-backend.git
cd video-editor-backend
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate (Mac/Linux)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a `.env` file:
```
DATABASE_URL=postgresql://youruser:yourpass@localhost:5432/videoeditor
```

### 5. Create the PostgreSQL database
```sql
CREATE DATABASE videoeditor;
```

---

## ▶️ Run the app
```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 📦 API Endpoints

### ➕ Upload Video
```
POST /api/videos/upload
```
- form-data: `file=<video>`

### ✂️ Trim Video
```
POST /api/videos/{id}/trim
```
- JSON body: `{ "start": 3, "end": 15 }`

### 💬 Add Subtitles
```
POST /api/videos/{id}/subtitles
```
- JSON body: `{ "text": "Hello!", "start": 3, "end": 6 }`

### 🧪 Render Final Video
```
POST /api/videos/{id}/render
```

### 📥 Download Final Video
```
GET /api/videos/{id}/download
```


