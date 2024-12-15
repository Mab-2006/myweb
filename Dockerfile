# استفاده از یک تصویر پایه پایتون
FROM python:3.9-slim

# نصب پکیج‌های مورد نیاز لینوکس (برای مثال، اگر به پکیج‌های خاصی نیاز دارید)
RUN apt-get update && apt-get install -y libpq-dev

# کپی کردن فایل‌های پروژه به داخل کانتینر
COPY . /app/.

# تعیین دایرکتوری کاری
WORKDIR /app

# نصب وابستگی‌ها از فایل requirements.txt
RUN pip install -r requirements.txt

# اجرای دستور پیش‌فرض برای پروژه
CMD ["python", "server.py"]
