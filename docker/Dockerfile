# تصویر پایه سبک
FROM python:3.9-slim

# کاربر غیر روت
RUN adduser --disabled-password --gecos '' appuser

# پوشه کاری
WORKDIR /app

# کپی و نصب پکیج‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# کپی کد پروژه
COPY ./app ./app
COPY ./app/models ./app/models

# تغییر کاربر
USER appuser

# پورت
EXPOSE 80

# اجرای FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "2"]

