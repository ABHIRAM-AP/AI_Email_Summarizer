# AI Email Summarizer 📧

An AI-powered application that automatically fetches emails, summarizes their content using a **Hugging Face Transformer model (BART Large CNN)**, and delivers concise summaries directly to **Telegram**.

This project helps reduce email overload by converting long emails into short, meaningful summaries.

---

##  Features

-  Automatically fetches emails from inbox
-  AI-based email summarization using **facebook/bart-large-cnn**
-  Supports **GPU acceleration** (if available)
-  Sends summarized content to Telegram
-  Modular and extensible Python codebase

---

##  Tech Stack

- **Python 3**
- **Email Fetching**: IMAP
- **AI Model**: Hugging Face Transformers  
  - Model: `facebook/bart-large-cnn`
- **ML Framework**: PyTorch
- **Messaging**: Telegram Bot API

---

##  Project Structure

```text
AI_Email_Summarizer/
│
├── main.py               # Application entry point
├── fetch_email.py        # Fetches emails from inbox using IMAP
├── email_summarizer.py   # AI summarization logic using BART
├── telegram_send.py      # Sends summaries to Telegram
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
