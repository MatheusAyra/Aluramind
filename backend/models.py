from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    feedback_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_id = db.Column(db.String(50), db.ForeignKey('feedback.id'), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
