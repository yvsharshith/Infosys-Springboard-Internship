import os
import requests
import sys
import PyPDF2
import docx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

def read_text_or_file(title):
    print(f"\n--- {title} ---")
    print("Choose input method:")
    print("1) Paste text manually")
    print("2) Provide file path (.txt / .pdf / .docx)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print("\nPaste the text below. Enter a blank line to finish:\n")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == "2":
        path = input("Enter file path: ").strip()
        if not os.path.exists(path):
            print("File not found. Try again.")
            return read_text_or_file(title)
        return read_file(path)

    else:
        print("Invalid choice. Try again.")
        return read_text_or_file(title)

# file reading
def read_file(path):
    if path.endswith(".txt"):
        return read_txt(path)
    elif path.endswith(".pdf"):
        return read_pdf(path)
    elif path.endswith(".docx"):
        return read_docx(path)
    else:
        print("Unsupported file format. Only .txt, .pdf, .docx allowed.")
        sys.exit(1)


def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def read_pdf(path):
    if not PyPDF2:
        print("PyPDF2 not installed. Run: pip install PyPDF2")
        sys.exit(1)

    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


def read_docx(path):
    if not docx:
        print("python-docx not installed. Run: pip install python-docx")
        sys.exit(1)

    doc = docx.Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text

# api calling
def ask_groq(job_desc, resume):
    prompt = f"""
You are a job matching assistant.
Compare the job description and resume.

Job Description:
{job_desc}

Resume:
{resume}

Answer these:
- Match percentage (0-100)
- Matching skills
- Missing skills
- Whether the candidate should apply
    """

    response = requests.post(
        URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a job evaluation assistant."},
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()

    if "error" in data:
        return "API Error: " + str(data["error"])

    return data["choices"][0]["message"]["content"]

def main():
    job_desc = read_text_or_file("Job Description")
    resume = read_text_or_file("Resume")

    print("\nAnalyzing...\n")
    result = ask_groq(job_desc, resume)

    print("=== RESULT ===")
    print(result)


if __name__ == "__main__":
    main()
