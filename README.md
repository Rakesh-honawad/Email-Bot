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
