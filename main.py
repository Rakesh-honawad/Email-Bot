import os
import fitz  # PyMuPDF
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import sys
import io

# Optional: Force UTF-8 output for Windows terminal
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
except Exception as e:
    print("Encoding override failed:", e)

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Debug: Check env values
if not SENDER_EMAIL or not EMAIL_PASSWORD:
    print(" Missing environment variables. Check .env file.")
    exit(1)

def extract_rows_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    lines = text.strip().split('\n')
    rows = []
    for line in lines[1:]:  # Skip header line
        parts = [p.strip() for p in line.split(',')]
        if len(parts) >= 3:
            name, email, company = parts[:3]
            rows.append({"name": name, "email": email, "company": company})
        else:
            print(f" Skipping malformed line: {line}")
    return rows

def load_email_template():
    template_path = "templates/email_template.txt"
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Email template not found: {template_path}")
    
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def fill_template(template, name, company):
    return template.replace("{{name}}", name).replace("{{company}}", company)

def send_email(to_email, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    # Attach resume if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    elif attachment_path:
        raise FileNotFoundError(f"Attachment not found: {attachment_path}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f" Email sent to {to_email}")

def main():
    pdf_path = "recipients.pdf"
    resume_path = "Rakesh_Honawad.pdf"
    subject = "Inquiry About Any Open SDE Positions"
    
    template = load_email_template()
    recipients = extract_rows_from_pdf(pdf_path)

    if not recipients:
        print(" No valid recipients found in the PDF.")
        return

    for person in recipients:
        email_body = fill_template(template, person["name"], person["company"])
        try:
            send_email(person["email"], subject, email_body, attachment_path=resume_path)
        except Exception as e:
            print(f" Failed to send email to {person['email']}: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f" Uncaught error: {e}")
