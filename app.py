from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rp6eVkQdZK:06xjLGmkcg@remotemysql.com/rp6eVkQdZK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)

'''@app.route("/")
def hello_world():
    return render_template('index.html')'''

@app.route("/", methods=['GET','POST'])
def df():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        try:
            msg1 =  name + "\n" + email + "\n" + message
            msg2 = "Thank you for contacting me."
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("ankitapatra162001@gmail.com","8372923795")
            server.sendmail("ankitapatra162001@gmail.com", "ankitapatra162001@gmail.com", msg1)
            server.sendmail("ankitapatra162001@gmail.com", email, msg2)
            print("Mail sent")
            contact=Contact(name=name, email=email, message=message)
            db.session.add(contact)
            db.session.commit()
            print("Saved in db")
            return redirect("/")
        except Exception as e:
            print(e)

    contact1 = Contact.query.all()
    return render_template('index.html', contacts=contact1)

if __name__ == '__main__':
    app.run(debug=True)