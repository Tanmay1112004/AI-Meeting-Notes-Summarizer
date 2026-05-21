
# 📝 AI Meeting Notes Summarizer

An intelligent meeting assistant that automatically extracts key points, decisions, and action items from meeting transcripts using Google's Gemini AI.

## ✨ Features

- 📄 **Multi-format support** - Upload TXT, PDF, or DOCX files
- 🤖 **AI-powered analysis** - Uses Google Gemini 1.5 Flash for intelligent summarization
- 📊 **Structured output** - Get summaries, key decisions, action items, and next steps
- 🎨 **Clean interface** - Built with Streamlit for an intuitive user experience
- 📥 **Export results** - Download summaries as text files
- 🔒 **Secure** - Your API key stays local (no server-side storage)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Click "Get API key" and create a new key
   - Copy the generated key

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run meeting_summarizer.py
   ```

6. **Open your browser** - The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Prepare your meeting transcript** - Save as TXT, PDF, or DOCX
2. **Upload the file** using the file picker
3. **Click "Generate Meeting Summary"** 
4. **Review the AI analysis** including:
   - Meeting summary
   - Key decisions
   - Action items with assignees
   - Next steps
5. **Download the summary** for sharing with your team

### Sample Input Format

The AI works best with structured meeting notes like:
```
Meeting: Project Name
Date: May 20, 2026
Attendees: Name1 (Role), Name2 (Role)

Discussion points...
Decisions made...
Action items...
```

## 🧪 Testing

A sample meeting transcript is provided above in the README. Save it as `sample_meeting.txt` to test the application:

1. Copy the sample transcript from the "Testing" section above
2. Save as `sample_meeting.txt`
3. Upload to the app
4. Generate your first summary

## 📁 Project Structure

```
meeting-summarizer/
├── meeting_summarizer.py   # Main application
├── requirements.txt         # Python dependencies
├── .env                     # API key (create this)
├── sample_meeting.txt       # Test file (optional)
└── README.md               # This file
```

## 🛠️ Tech Stack

- **Frontend/UI** - Streamlit
- **AI Model** - Google Gemini 1.5 Flash
- **Document Processing** - PyPDF2, python-docx
- **Environment Management** - python-dotenv

## 📝 Example Output

```
**Summary:** The team discussed Q3 marketing strategy, focusing on social media campaigns and budget allocation. Key points included LinkedIn ad performance and content calendar planning.

**Key Decisions:**
- Budget increased by 15% for LinkedIn ads
- Launch date set for July 15th
- Dark mode feature moved to Q4

**Action Items:**
- Sarah: Prepare creative assets by June 30th
- Mike: Finalize targeting parameters by July 5th
- Priya: Set up early access waitlist page

**Next Steps:**
- Load test scheduled for July 5th
- Beta build target: June 25th
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| API key error | Check your `.env` file has `GEMINI_API_KEY=your_key` (no quotes) |
| File too large | Gemini handles up to 1M tokens, but very large files may be slow |
| No output | Ensure transcript has enough content (minimum 100 characters) |
| Import errors | Run `pip install -r requirements.txt` again |

## 🔒 Privacy & Security

- Your API key is stored locally in `.env` (never uploaded)
- Files are processed locally and sent only to Google's Gemini API
- No data is stored permanently by the application
- Review Google's [Gemini API privacy policy](https://ai.google.dev/gemini-api/terms) for details

## 🚧 Future Enhancements

- [ ] Audio/voice transcription using Whisper
- [ ] Email export functionality
- [ ] Multiple meeting formats (Zoom, Google Meet exports)
- [ ] Custom prompt templates
- [ ] Meeting sentiment analysis
- [ ] Searchable meeting archive
- [ ] Collaborative editing of summaries

## 🤝 Contributing

Feel free to submit issues, fork the repository, or create pull requests with improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- UI powered by [Streamlit](https://streamlit.io/)
- Inspired by real-world meeting productivity challenges

## 📧 Support

For issues or questions:
1. Check the Common Issues table above
2. Verify your API key is active in Google AI Studio
3. Ensure all dependencies are installed correctly

---

**Made with ❤️ for productive meetings**
```

---

This README includes:
- Project overview and features
- Step-by-step setup instructions  
- Usage guide with examples
- Testing instructions
- Troubleshooting table
- Privacy information
- Future roadmap

Save this as `README.md` in your project folder alongside the other files. Your project is now complete with all three files: `requirements.txt`, `meeting_summarizer.py`, and `README.md`!