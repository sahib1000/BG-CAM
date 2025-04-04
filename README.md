# 📸 AI Passport Photo Web App

This is a Flask-based web application that allows users to capture their photo, remove the background using the [Remove.bg API](https://www.remove.bg/api), and download the final result as a **PDF**.

> ✅ Made for passport photo creation with camera capture, background removal, and PDF generation.

---

## 🔧 Features

- 📷 Capture photo directly from camera
- 🧼 AI-based background removal using Remove.bg
- 🖼️ Manual cropping (user-controlled)
- 📄 Download final image as PDF
- 🚀 Easy to deploy on Render

---

## 🧠 Tech Stack

- Frontend: HTML, JavaScript
- Backend: Python Flask
- AI APIs:  
  - Background Removal: [Remove.bg](https://www.remove.bg/api)

---

## 🚀 How to Deploy on Render (Free Hosting)

1. **Fork or Clone this repository**
2. Make sure you have these files:
   - `app.py`
   - `templates/index.html`
   - `requirements.txt`
3. Upload the repo to [GitHub](https://github.com)

### 🛠️ On [Render](https://render.com):
1. Create a free account
2. Click on **"New > Web Service"**
3. Connect your GitHub repo
4. Fill these values:

| Setting             | Value                                |
|---------------------|--------------------------------------|
| Build Command       | `pip install -r requirements.txt`    |
| Start Command       | `gunicorn app:app`                   |
| Runtime             | Python 3.10                          |

5. Add environment variables:

| Key                 | Value                            |
|---------------------|----------------------------------|
| `REMOVE_BG_API_KEY` | Your remove.bg API key           |

---

## 🖼️ Screenshot

![App Screenshot](https://via.placeholder.com/700x400?text=Passport+Photo+App+Preview)

---

## 🧪 Local Setup (Optional)

```bash
git clone https://github.com/your-username/passport-photo-app.git
cd passport-photo-app
pip install -r requirements.txt
python app.py
