import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from docx import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_txt(file):
    return file.read().decode("utf-8")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()
    
    if file_type == "txt":
        return extract_text_from_txt(uploaded_file)
    elif file_type == "pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload .txt, .pdf, or .docx")

def summarize_meeting(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are an AI meeting assistant. Analyze the following meeting transcript and provide:
    
    1. **Summary** (2-3 paragraphs covering main discussion points)
    2. **Key Decisions** (bullet points)
    3. **Action Items** (bullet points with responsible person if mentioned)
    4. **Next Steps** (bullet points)
    
    Transcript:
    {text[:30000]}  # Gemini 1.5 Flash has 1M token context, but keeping reasonable for speed
    """
    
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI Meeting Summarizer", page_icon="📝", layout="wide")

st.title("📝 AI Meeting Notes Summarizer")
st.markdown("Upload your meeting transcript (.txt, .pdf, .docx) and get AI-powered summaries, action items, and decisions.")

with st.sidebar:
    st.header("About")
    st.info(
        "This app uses **Google Gemini API** to analyze meeting transcripts.\n\n"
        "Features:\n"
        "- 📄 Extract text from TXT, PDF, DOCX\n"
        "- 📊 Generate structured summaries\n"
        "- ✅ Extract action items\n"
        "- 🎯 Highlight key decisions\n\n"
        "**Setup:** Create a `.env` file with `GEMINI_API_KEY=your_key_here`"
    )
    
    st.markdown("---")
    st.caption("Built with Streamlit + Gemini API")

uploaded_file = st.file_uploader(
    "Choose a meeting transcript file",
    type=["txt", "pdf", "docx"],
    help="Upload any meeting transcript or notes file"
)

if uploaded_file:
    with st.spinner("Extracting text from file..."):
        try:
            transcript_text = extract_text_from_file(uploaded_file)
            st.success(f"✅ File loaded successfully! ({len(transcript_text)} characters)")
            
            with st.expander("Preview extracted text"):
                st.text(transcript_text[:1000] + ("..." if len(transcript_text) > 1000 else ""))
            
            if st.button("🎯 Generate Meeting Summary", type="primary", use_container_width=True):
                with st.spinner("Analyzing with Gemini AI... (takes a few seconds)"):
                    try:
                        summary = summarize_meeting(transcript_text)
                        
                        # Display results in clean format
                        st.markdown("---")
                        st.markdown("## 📋 Meeting Analysis Report")
                        
                        # Parse and display (Gemini returns markdown-friendly text)
                        st.markdown(summary)
                        
                        # Download button
                        st.markdown("---")
                        st.download_button(
                            label="📥 Download Summary as Text",
                            data=summary,
                            file_name="meeting_summary.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"Error during summarization: {str(e)}")
                        st.info("Please check your Gemini API key and try again.")
                        
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
else:
    st.info("👈 Upload a meeting transcript file to get started!")
    
    # Example placeholder
    st.markdown("### Sample output preview:")
    st.markdown("""
    **Summary:** The team discussed Q3 marketing strategy, focusing on social media campaigns...
    
    **Key Decisions:**
    - Budget increased by 15% for LinkedIn ads
    - Launch date set for July 15th
    
    **Action Items:**
    - Sarah: Prepare creative assets by June 30th
    - Mike: Finalize targeting parameters by July 5th
    """)