# 🧾 Bank Statement Analyzer with Gemini AI

This Python project analyzes Chase (or any bank) CSV statements and uses **Google Gemini AI** to classify each **debit** transaction as a _"need"_ or _"want"_ based on its description.

---

## 🚀 Features

- Parses a CSV bank statement
- Filters for **DEBIT** transactions
- Uses **Google Gemini (Generative AI)** to label each as **"need"** or **"want"** and adds as a data type
- Future Additions
    - Visualize Data in order for user to see the spread of their tranactions
    - Add AI chatbot to help you understand your spendings and how to spend in the future according to your situation

---

## 📦 Requirements

- Python 3.8+
- Google Generative AI Python SDK
- A Google API key for **Gemini Pro** access(If not, there is exception handling in order to combact low request rate)

### 🔧 Install Dependencies

```bash
pip install pandas numpy python-dotenv google-generativeai

