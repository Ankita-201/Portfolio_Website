from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://29iTJEKLOB:JmMtxA9wmQ@remotemysql.com/29iTJEKLOB'
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

        contact=Contact(name=name, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        return redirect("/")

    contact1 = Contact.query.all()
    return render_template('index.html', contact=contact1)

if __name__ == '__main__':
    app.run(debug=True)