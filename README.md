📧 Auto Email Sender Using PDF Contact List
This Python project automates the process of sending customized emails with attachments. It extracts recipient data (name, email, company) from a PDF file, fills a dynamic email template, and sends each recipient a personalized message with your resume attached.

🛠 Features
🔍 Extracts structured data from a PDF (recipient list)

🧩 Fills an email template using placeholders (e.g., {{name}}, {{company}})

📎 Attaches a PDF resume to each email

🔐 Uses environment variables for secure Gmail credentials

✅ Sends emails via Gmail SMTP (smtplib) with SSL

📁 Project Structure
Edit
📦 auto-email-sender
├── main.py
├── recipients.pdf             # PDF with Name, Email, Company in comma-separated format
├── Rakesh_Honawad.pdf         # Resume to attach
├── templates/
│   └── email_template.txt     # Template with {{name}} and {{company}} placeholders
├── .env                       # Stores SENDER_EMAIL and EMAIL_PASSWORD
├── README.md
📦 Requirements
Make sure you have the following installed:
pip install python-dotenv pymupdf
📄 .env Format
Create a .env file in the root directory with:
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password  # Use App Password if 2FA is enabled
📤 How to Run
python main.py
✅ The script will:

Read the recipient list from recipients.pdf

Fill the email template from templates/email_template.txt

Attach your resume Rakesh_Honawad.pdf

Send personalized emails using Gmail SMTP

🧪 Email Template Example
templates/email_template.txt

arduino
Copy
Edit
Dear {{name}},

I hope this message finds you well. I'm reaching out to inquire about any open opportunities at {{company}}. Please find my resume attached.

Best regards,
Rakesh Honawad
⚠️ Notes
Make sure less secure app access is enabled or use App Password with 2FA Gmail.

The PDF (recipients.pdf) must have comma-separated values in this order:
Name, Email, Company
