# 📧 Intelligent Email Router (FastAPI)

این پروژه یک API ساده برای **دسته‌بندی ایمیل‌ها** با استفاده از **FastAPI + scikit-learn** است.  
مدل با داده‌های نمونه آموزش داده می‌شود و سپس در API بارگذاری می‌شود.

---

## 🚀 راه‌اندازی محلی
```bash
# ساخت محیط مجازی
python -m venv .venv
source .venv/bin/activate   # در ویندوز: .venv\Scripts\activate

# نصب پکیج‌ها
pip install -r requirements.txt

# آموزش مدل
python training/train.py

# اجرای API
uvicorn app.main:app --reload
