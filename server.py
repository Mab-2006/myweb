from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from flask_sqlalchemy import SQLAlchemy
import subprocess


app = Flask(__name__)
app.secret_key = "secret-key"



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

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

def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(ADMIN_EMAIL, ADMIN_PASSWORD)

        message = MIMEMultipart()
        message["From"] = ADMIN_EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server.sendmail(ADMIN_EMAIL, to_email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("This email is already registered.", 'error')
            return redirect(url_for('register'))

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        user_subject = "Welcome to Our Platform!"
        user_body = f"Hi {first_name} {last_name},\n\nThank you for registering on our platform.\n\nBest regards,\nMohammadAminBaranzehi"
        send_email(email, user_subject, user_body)

        admin_subject = "New User Registration"
        admin_body = f"A new user has registered:\n\nName: {first_name} {last_name}\nEmail: {email}\nPassword: {password}"
        send_email(ADMIN_EMAIL, admin_subject, admin_body)

        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            return redirect(url_for('home'))
        else:
            flash("Invalid login credentials", 'error')
            return redirect(url_for('login.html'))

    return render_template('templates/login.html')


@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
