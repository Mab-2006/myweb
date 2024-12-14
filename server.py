from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

app = Flask(__name__)
app.secret_key = "secret-key"  # For flash messages

# Gmail credentials
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()
ADMIN_EMAIL = config['admin_email']
ADMIN_PASSWORD = config['admin_password']
user_subject = config['user_subject']
user_body = config['user_body']
admin_subject = config['admin_subject']
admin_body = config['admin_body']

# Function to send emails
def send_email(to_email, subject, body):
    try:
        # Setting up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(ADMIN_EMAIL, ADMIN_PASSWORD)

        # Creating the email
        message = MIMEMultipart()
        message["From"] = ADMIN_EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Sending the email
        server.sendmail(ADMIN_EMAIL, to_email, message.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Route for the registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Save or process user data
        print(f"New user registered: {first_name} {last_name}, Email: {email}")

        # Sending a welcome email to the user
        user_subject = "Welcome to Our Platform!"
        user_body = f"Hi {first_name} {last_name},\n\nThank you for registering on our platform.\n\nBest regards,\nMohammadAminBaranzehi"
        send_email(email, user_subject, user_body)

        # Sending user info to admin
        admin_subject = "New User Registration"
        admin_body = f"A new user has registered:\n\nName: {first_name} {last_name}\nEmail: {email}\nPassword: {password}"
        send_email(ADMIN_EMAIL, admin_subject, admin_body)

        # Flash message and redirect to a welcome page
        flash(f"Welcome {first_name} {last_name}! Registration successful.", "success")
        return redirect(url_for('welcome'))
    return render_template('register.html')

# Route for the welcome page
@app.route('/welcome')
def welcome():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
