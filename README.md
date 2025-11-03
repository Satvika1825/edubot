# 🧠 EduBot – AI-Powered Study Assistant

Built **EduBot**, an AI-powered study companion designed to help **students** and **teachers** learn, teach, and stay motivated — developed as part of the **#ADKHackathon**!

---

## 🚀 Features

* 🔐 **Secure Login** with Firebase Authentication
* 📘 **Subject-wise Explanations** – Get detailed answers tailored to your subject
* 🤖 **AI Doubt Solving** – Ask any question and receive instant, intelligent help
* 🧩 **Quiz & Progress Tracking** – Test your knowledge and monitor performance
* 💬 **Motivation Agent** – Boosts student morale with personalized encouragement

---

## 🛠️ Tech Stack

| Component       | Technology          |
| --------------- | ------------------- |
| Frontend        | Streamlit           |
| Backend         | Python              |
| Database & Auth | Firebase            |
| Data Models     | Pydantic            |
| Integration     | ADK-Compatible Flow |

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Satvika1825/edubot.git
   cd edubot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # (Windows)
   source venv/bin/activate  # (Mac/Linux)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following:

```
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
FIREBASE_PROJECT_ID=your_firebase_project_id
```

---

## 🎯 Purpose

EduBot is built to:

* Simplify learning through intelligent assistance
* Empower teachers with AI-driven feedback
* Keep students motivated and progressing consistently



⭐ *If you like EduBot, give it a star on GitHub to support the project!*
