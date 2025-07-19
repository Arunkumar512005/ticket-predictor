"# Ticket Category Predictor using Flask" 
Here is the full **README.md** text you can directly copy and paste into your project folder:

---

````markdown
# 🧠 Smart Ticket Category Predictor 🎫  
A secure, full-stack Flask web app that predicts the category of customer support tickets using a machine learning model. Built with JWT authentication, PostgreSQL, and a simple HTML frontend.

---

## 🚀 Features

✅ User registration and login (JWT-based)  
✅ Secure prediction route (`/predict-ticket-category`)  
✅ ML model to classify ticket messages (e.g., refund, technical, account)  
✅ PostgreSQL database integration using SQLAlchemy  
✅ Frontend with login, register, and prediction UI  
✅ Swagger documentation (Flasgger)  
✅ Logging and error handling

---

## 🧰 Tech Stack

- **Backend**: Flask, Flask-JWT-Extended, SQLAlchemy, PostgreSQL  
- **Frontend**: HTML + CSS + JavaScript (vanilla)  
- **ML Model**: scikit-learn (Naive Bayes + Tfidf)  
- **Docs**: Flasgger (Swagger UI)  
- **Deployment**: Render / Railway / Localhost

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ticket-predictor.git
cd ticket-predictor
````

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` or config.py

```python
# config.py
DATABASE_URL = "postgresql://username:password@localhost/dbname"
JWT_SECRET_KEY = "your_jwt_secret"
```

### 5. Train the Model

```bash
python train_model.py
```

### 6. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 API Endpoint

### 🔐 `POST /predict-ticket-category`

```http
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "message": "My refund hasn't arrived"
}
```

Response:

```json
{
  "user": "arun",
  "message": "My refund hasn't arrived",
  "predicted_category": "Refund"
}
```

---

## 📁 Project Structure

```
.
├── app.py                # Main Flask app
├── auth.py               # Auth Blueprint
├── models.py             # User DB model
├── train_model.py        # ML model training
├── config.py             # Config (DB, secret)
├── model/
│   └── ticket_model.pkl  # Trained ML model
├── templates/
│   ├── login.html
│   ├── register.html
│   └── predict.html
├── static/
│   └── style.css
├── logs/
│   └── app.log
└── requirements.txt
```

---

## 👨‍💻 Author

**Arun Kumar**
Hackathon Participant • AI & Backend Enthusiast
 [GitHub](https://github.com/Arunkumar512005)

---

## 🏁 Future Improvements

* 📊 Admin dashboard for analytics
* 🔁 Refresh token + logout system
* 🧠 Improve model with larger dataset
* 🌍 Deploy to Render or GCP

---

## 🛡️ License

MIT License

```

---

Let me know if you want a `requirements.txt` generated for your project or want help pushing this to GitHub.
```
