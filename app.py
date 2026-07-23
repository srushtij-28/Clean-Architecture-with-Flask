from flask import Flask
from models import db
from controllers import user_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///users.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user_bp)

@app.route("/health")
def health():

    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(debug=True)
