from flask import Flask, request, jsonify, render_template, redirect
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import joblib
import logging

from config import DATABASE_URL, JWT_SECRET_KEY
from auth import auth_bp
from models import db

from flasgger import Swagger

# ✅ Setup logging
logging.basicConfig(level=logging.INFO, filename="logs/app.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Flask app init
app = Flask(__name__, template_folder="templates", static_folder="static")

# ✅ Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

# ✅ Initialize extensions
CORS(app)
db.init_app(app)
jwt = JWTManager(app)
swagger = Swagger(app)
app.register_blueprint(auth_bp)

# ✅ Load trained model
model = joblib.load("model/ticket_model.pkl")

# ✅ Create DB tables
with app.app_context():
    db.create_all()

# ✅ Frontend routes
@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route("/predict", methods=["GET"])
def predict_page():
    return render_template("predict.html")

# ✅ JWT-protected prediction API
@app.route("/predict-ticket-category", methods=["POST"])
@jwt_required()
def predict_ticket_category():
    """
    Predict support ticket category using ML model
    ---
    tags:
      - Prediction
    parameters:
      - name: message
        in: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: "My refund has not arrived"
    responses:
      200:
        description: Predicted category
        schema:
          type: object
          properties:
            predicted_category:
              type: string
      401:
        description: Unauthorized
    """
    try:
        data = request.get_json()
        message = data.get("message")

        if not message:
            return jsonify({"msg": "Message is required"}), 400

        prediction = model.predict([message])[0]

        logging.info(f"User: {get_jwt_identity()} - Message: {message} - Prediction: {prediction}")

        return jsonify({
            "user": get_jwt_identity(),
            "message": message,
            "predicted_category": prediction
        })
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return jsonify({"msg": "Internal server error"}), 500

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)
