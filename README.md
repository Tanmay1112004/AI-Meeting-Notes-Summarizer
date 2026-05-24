# 📝 AI Meeting Notes Summarizer

An AI-powered meeting assistant that automatically converts meeting transcripts into **structured summaries, key decisions, and action items** using **Google Gemini 1.5 Flash**.

Built with **Streamlit + Python**, designed for productivity, clarity, and real-world business use cases.

---

## ✨ Features

* 📄 Supports TXT, PDF, and DOCX files
* 🤖 AI-powered summarization using Gemini 1.5 Flash
* 🧠 Extracts key points, decisions, and action items
* 📊 Structured, easy-to-read output
* 📥 Download summary as text file
* 🎨 Simple Streamlit UI

---

## Demo Images

![demo](https://github.com/Tanmay1112004/AI-Meeting-Notes-Summarizer/blob/main/app_demo_images/Screenshot_21-5-2026_164116_supreme-space-acorn-g49w4jvxwppv39p7v-8501.app.github.dev.jpeg)

![demo]()

![demo]()

![demo]()

![demo]()

![demo]()

---

## 🚀 Quick Start

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Add API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 3️⃣ Run the app

```bash
streamlit run meeting_summarizer.py
```

---

## 🧠 How It Works

1. Upload meeting transcript (TXT/PDF/DOCX)
2. Text is extracted and cleaned
3. Gemini AI processes the content
4. Output is structured into:

   * Summary
   * Key Decisions
   * Action Items
   * Next Steps

---

## 🛠 Tech Stack

* Python
* Streamlit
* Google Gemini 1.5 Flash
* PyPDF2 / python-docx
* python-dotenv

---

## 📌 Example Output

* **Summary:** Project discussion on Q3 roadmap and planning
* **Key Decisions:** Budget approved, timeline finalized
* **Action Items:** Assign tasks to team members
* **Next Steps:** Execution planning and review

---

## 🔮 Future Enhancements

* 🎙️ Audio meeting transcription (Whisper)
* 📧 Email export
* 📊 Sentiment analysis
* 🔍 Meeting search history
* 🤝 Multi-user collaboration

---

## 👨‍💻 Author

**Tanmay Kshirsagar**
AI/ML & Full Stack Developer

---

## 📄 License

MIT License

---
