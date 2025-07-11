# 🔍 Suspicious Link Checker

A simple and lightweight Streamlit app that helps detect **suspicious or potentially dangerous links** using custom logic. Great for basic phishing protection, content moderation, and personal security checks.

---

## 🚀 Features

- ✅ Detects suspicious **keywords** like `free`, `gift`, `porn`, `login`, etc.
- 🌐 Flags dangerous **TLDs** like `.xyz`, `.tk`, `.click`
- 🔗 Warns against **link shorteners** like `bit.ly`, `t.co`, etc.
- 📋 Accepts multiple links at once (one per line)
- 🔒 No internet required — fully local, fast, and secure

---

## 🖥️ Demo Screenshot

![App Screenshot](https://via.placeholder.com/800x400.png?text=Suspicious+Link+Checker+Demo)

---

## 📦 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

---

## ⚙️ How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/Farhadali987/link-safety-checker.git
cd link-safety-checker
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install streamlit
Run the app:

bash
Copy
Edit
streamlit run simple_link_checker.py
🧠 Example
Input:

arduino
Copy
Edit
https://bit.ly/free-cash
https://google.com
Output:

❌ Dangerous: bit.ly/free-cash

✅ Safe: google.com

🤝 Credits
Developed by Engineer Farhad Ali Laghari
Agentic AI | Multilingual Bots | Open Source Contributor

📫 Contact
GitHub: Farhadali987

LinkedIn: Farhad Ali Laghari

🛡️ Disclaimer
This is a basic tool for educational use. Always use a full-fledged security scanner for critical applications.

yaml
Copy
Edit

---

### ✅ What To Do Now:

1. Save this as a new file in your project folder:  
   **`README.md`**

2. Then run in terminal:
```bash
git add README.md
git commit -m "Add project README"
git push
