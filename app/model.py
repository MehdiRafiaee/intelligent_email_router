from typing import Tuple, Optional
import joblib
import os
from pathlib import Path

MODEL_PATH = os.environ.get("MODEL_PATH", "/app/models/model.joblib")
_model = None

def load_model(path: Optional[str] = None):
    global _model
    path = path or MODEL_PATH
    p = Path(path)
    if p.exists():
        _model = joblib.load(path)
        print(f"[model] loaded from {path}")
    else:
        _model = None
        print("[model] no model found; predictions will return 'unknown'")

def predict_email_category(text: str) -> Tuple[str, float]:
    global _model
    if _model is None:
        return "unknown", 0.0
    try:
        pred = _model.predict([text])[0]
        conf = 1.0
        if hasattr(_model, "predict_proba"):
            probs = _model.predict_proba([text])[0]
            classes = list(_model.classes_)
            idx = classes.index(pred)
            conf = float(probs[idx])
        return str(pred), conf
    except Exception:
        return "error", 0.0
