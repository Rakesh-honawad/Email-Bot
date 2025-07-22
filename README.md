# 📧 Automated Email Bot using PDF Input & Python

This project is a **Python-based Email Automation Bot** that reads recipient data from a PDF file and sends **customized emails** with optional attachments (e.g., resume).  
It’s ideal for job outreach, marketing campaigns, or personalized bulk emailing.

---

## ✅ FEATURES

- 📄 Extracts recipient info (name, email, company) from a PDF  
- 📨 Sends personalized emails using a dynamic template  
- 📎 Supports optional attachments (like resume)  
- 🔐 Uses `.env` for secure credential management  
- 📜 Logs successes and failures per email sent  

---

## 🧰 TECH STACK

- **Python 3.x**  
- [`smtplib`](https://docs.python.org/3/library/smtplib.html)  
- [`email.message`](https://docs.python.org/3/library/email.message.html)  
- [`dotenv`](https://pypi.org/project/python-dotenv/)  
- [`PyMuPDF (fitz)`](https://pymupdf.readthedocs.io/en/latest/)  
- Gmail SMTP (or any SMTP provider)  

## ⚙️ SETUP INSTRUCTIONS

### 📦 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-bot-pdf.git
cd email-bot-pdf
```
### 🔐 Step 2: Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```env
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
```
### 📄step 3. Prepare the PDF File
Create a recipients.pdf file with this format:

```graphql
Name, Email, Company
Alice Johnson, alice@example.com, Amazon
Bob Smith, bob@example.com, Microsoft
```
📝 The first line is the header. Ensure data is comma-separated.
### 📝 4. Create the Email Template
In a templates folder, create email_template.txt:
```mathematica
Hi {{name}},

I'm reaching out regarding any potential opportunities at {{company}}.  
I believe my experience and skills align well with your team.

Looking forward to hearing from you.

Best regards,  
<your_name>
```
### ▶️ 5. Run the Bot
Make sure everything is set up, then run:
```bash
python main.py
Each recipient will receive a personalized email, with your resume attached if configured.
```
### 📁 PROJECT STRUCTURE
```bash
📦 email-bot-pdf
├── main.py
├── recipients.pdf
├── Rakesh_Honawad.pdf
├── .env
└── templates/
    └── email_template.txt
```
### 💡 USE CASES
🚀 Apply to multiple job openings with customized messages

💼 Outreach to recruiters and companies

📢 Personalized email marketing campaigns

### 🙌 AUTHOR
Built with 💙 by Rakesh Honawad

### ⭐ SUPPORT
If this project helped you, feel free to star ⭐ it on GitHub.
