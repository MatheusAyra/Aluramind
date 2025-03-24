from flask import Blueprint, request, jsonify, render_template
from backend.models import db, Feedback, FeatureRequest
from backend.sentiment_analysis import classify_sentiment
from backend.feature_extraction import extract_feature_requests

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route("/feedbacks", methods=["POST"])
def analyze_feedback():
    data = request.json
    feedback_id = data["id"]
    feedback_text = data["feedback"]

    sentiment = classify_sentiment(feedback_text)
    features = extract_feature_requests(feedback_text)

    # Salvar no banco
    feedback_entry = Feedback(id=feedback_id, feedback_text=feedback_text, sentiment=sentiment)
    db.session.add(feedback_entry)
    for feature in features:
        feature_entry = FeatureRequest(feedback_id=feedback_id, code=feature["code"], reason=feature["reason"])
        db.session.add(feature_entry)
    db.session.commit()

    return jsonify({
        "id": feedback_id,
        "sentiment": sentiment,
        "requested_features": features
    })

@feedback_bp.route("/report")
def report():
    total_feedbacks = Feedback.query.count()
    positive_feedbacks = Feedback.query.filter_by(sentiment="POSITIVO").count()
    features = FeatureRequest.query.with_entities(FeatureRequest.code, db.func.count()).group_by(FeatureRequest.code).all()

    positive_percentage = (positive_feedbacks / total_feedbacks) * 100 if total_feedbacks else 0
    top_features = [{"feature": f[0], "count": f[1]} for f in features]

    return render_template("report.html", positive_percentage=positive_percentage, top_features=top_features)
