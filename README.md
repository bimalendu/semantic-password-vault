---

````markdown
# 🔐 Semantic Password Vault

A secure, offline Streamlit application that allows you to semantically search through your exported browser passwords by website, username, or related context.

> ❗ **Disclaimer**: This tool is intended for personal use only. It does not store or transmit any data — everything runs locally on your machine. Please handle your exported password files with care.

---

## 🚀 Features

- ✅ Upload password CSVs exported from Chrome, Edge, or Firefox
- 🔎 Perform **semantic search** (not just keyword match)
- 📂 Load more results incrementally
- ⚡ Powered by [Sentence Transformers](https://www.sbert.net/) for fast and meaningful search
- 🛡️ 100% offline and secure

---

## 📦 Installation

1. **Clone the repo (or save the file)**

   ```bash
   git clone https://github.com/yourusername/semantic-password-vault.git
   cd semantic-password-vault
````

2. **Install dependencies**

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install packages:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually:

   ```bash
   pip install streamlit pandas sentence-transformers
   ```

---

## 📝 Usage

1. **Export your passwords** from your browser:

   * **Chrome / Edge**:
     Go to `chrome://settings/passwords` → ⋮ → `Export Passwords` → Save as `.csv`

   * **Firefox**:
     Firefox does not export passwords natively. You can use an extension or third-party tool to export to `.csv`.

2. **Run the app**:

   ```bash
   streamlit run password_vault.py
   ```

3. **Upload the `.csv` file** using the interface and start searching semantically!

---

## 📁 File Structure

```
semantic-password-vault/
├── password_vault.py         # Main Streamlit app
├── requirements.txt          # Python dependencies
└── README.md                 # You're here!
```

---

## ✅ Roadmap / To-Do

* [ ] Password masking / toggle visibility
* [ ] Export filtered results
* [ ] Support encrypted local storage
* [ ] Multi-browser format detection
* [ ] Dark mode toggle

---

## 🔐 Security

* No data is stored or transmitted.
* All processing happens **locally in memory**.
* Password files are never uploaded or cached by the app.
* Still: **Handle your exported CSV with extreme care.**

---

## 🧠 Powered By

* [Streamlit](https://streamlit.io/)
* [Sentence Transformers](https://www.sbert.net/)
* [pandas](https://pandas.pydata.org/)

---

## 📝 License

MIT License

---

## 🙋 FAQ

### ❓ Can this app automatically pull passwords from my browser?

No. This app is designed to avoid accessing system-level password managers or secure storage. You must **export your data manually** for safety and legal reasons.

### ❓ Is my data safe?

Yes. The app never stores or sends your data. It runs entirely in your local Python environment.

---

## 📬 Contact

Created by [Bimal](https://github.com/bimalendu) — PRs, feedback, and contributions welcome!
Let me know if you'd like a version with Docker support, encrypted storage, or a hosted demo (if sanitized).
