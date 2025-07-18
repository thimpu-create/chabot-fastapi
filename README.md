# 🤖 Desi Babu Chatbot

A friendly chatbot built using **LLaMA 3.0**, **Gradio**, and **FastAPI** — that talks like your local Assamese buddy, full of desi vibes and slang! 🇮🇳💬

---

## 🚀 Tech Stack

- 🧠 **LLaMA 3.0** via Hugging Face
- 🌐 **FastAPI** to launch the app
- 🎨 **Gradio** for a beautiful UI
- 🔒 Hugging Face Token via `.env`

---

## ⚙️ Setup Instructions

### 1. 📁 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows
```

### 2. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 3. 🔐 Get your Hugging Face Token

1. Create a Hugging Face account  
2. Visit: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
3. Copy your token

Now, create a `.env` file in your root directory and add:

```env
token="your_huggingface_token_here"
```

### 4. 🚀 Run the FastAPI App

```bash
uvicorn main:app --reload
```

> ⚠️ This also launches the Gradio app on **port 7860**

---

## 🖥️ Access the Chatbot

Once running, open your browser and go to:

```
👉 http://localhost:7860
```

You’ll be greeted with a fun, desi-themed chatbot!

---

## 🧠 How It Talks

This bot behaves like your **Assamese bestie**:

- Sprinkles in local slang
- Always chill, always vibing 😎
- Talks like a human, but smarter 😏

---

## 📸 Preview

_✨ Coming soon... screenshot or GIF preview here!_

---

## 🔮 Upcoming Features

- ✅ Conversation memory
- ✅ Voice chat (beta)
- ✅ Slang-mode toggle
- ✅ More desi language packs

---

## 📜 License

**MIT License**

Use it, remix it, fork it — just give credit to your desi dev 🤘

---

## 💖 Made with Love

By your local techie — fueled by code, chai, and chill 🫖

---

_Star this repo if you vibe with it! ⭐_
