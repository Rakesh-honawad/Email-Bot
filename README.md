# 📧 Automated Email Bot using PDF Input & Python

This project is a **Python-based Email Automation Bot** that reads recipient data from a PDF file and sends **customized emails** with optional attachments (e.g., resume).  
Built using `smtplib`, `email`, `dotenv`, and `PyMuPDF`, it’s ideal for job outreach, marketing campaigns, or personalized bulk emailing.

---

## ✅ FEATURES

- 📄 **Extracts recipient info** (name, email, company) from PDF
- 📨 **Sends customized emails** using a dynamic template
- 📎 Optional attachment support (like resume)
- 🔐 Uses environment variables for secure credential management
- 🔁 Logs success and failures for each email sent

---

## 🧰 TECH STACK

- **Python 3.x**
- `smtplib` for sending emails
- `email.message` for composing MIME messages
- `dotenv` for secure environment variable handling
- `PyMuPDF (fitz)` for reading from PDF
- `Gmail SMTP` (can be adapted to other SMTP providers)

---

## ⚙️ SETUP INSTRUCTIONS

### 📦 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-bot-pdf.git
cd email-bot-pdf

---

### 🔐 2. Configure Environment Variables

Create a `.env` file in the root directory of your project and add the following:

```env
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password

📄 3. Prepare the PDF File
Create a file named recipients.pdf with the following comma-separated format:
Name, Email, Company
Alice Johnson, alice@example.com, Amazon
Bob Smith, bob@example.com, Microsoft
📝 Ensure the first line is the header and data begins from the second line.
