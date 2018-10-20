from flask import Flask,session, request, flash, url_for, redirect, render_template
from forms import Registration, LogIn
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user , logout_user , current_user , login_required, LoginManager

#for future config.py----------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testfile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#edit this as postgresql://user:pass@host/bookIIT
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/bookIIT'
app.static_folder = 'static'

db = SQLAlchemy(app)
#for future config.py----------
#for future models.py----------
class Acc(db.Model):
    __tablename__ = "account"
    id = db.Column('acc_id', db.Integer , primary_key=True)
    type = db.Column('acc_type', db.Integer)
    username = db.Column('username', db.String(), unique=True, index=True)
    password = db.Column('password', db.String())
    email = db.Column('email', db.String(), unique=True, index=True)

    def __init__(self, username, password, email):
        self.username = username
        self.type = 0;
        self.password = password
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Acc %r>' % (self.username)

class User(db.Model):
    __tablename__ = "user_acc"
    id = db.Column('user_id', db.Integer , primary_key=True)
    fname = db.Column('fname', db.String())
    lname = db.Column('lname', db.String())
    contact = db.Column('contact', db.String())

    def __init__(self, id, fname, lname, contact):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.contact = contact
#for future models.py----------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "You have logged out."

@app.route("/")

@app.route("/index", methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route("/landing")
@login_required
def landing():
    return render_template('landing.html')

@app.route("/addvenue", methods=['GET'])
@login_required
def addvenue():
    return render_template('addvenue.html')

@app.route("/venue", methods=['GET'])
@login_required
def venue():
    return render_template('venue.html')

@app.route("/logout")
@login_required
def logout():
    flash('You have logged out!')
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        form = Registration()
        return render_template('register.html', title='Register', form=form)
    newacc = Acc(request.form['username'],request.form['pass'],request.form['email'])
    user = User(Acc.get_id(newacc),request.form['fname'], request.form['lname'],request.form['email'])
    db.session.add(newacc)
    db.session.add(user)
    db.session.commit()
    flash('Account created for {form.username.data}!')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['pass']
    registered_user = Acc.query.filter_by(email=email,password=password).first()
    if registered_user is None:
        flash('Email or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    #return redirect(request.args.get('next') or url_for('main'))
    return render_template('landing.html')

@login_manager.user_loader
def load_user(acc_id):
    reg_user = Acc.query.filter_by(id=acc_id).first()
    #User.query.get(int(acc_id))
    return reg_user

if __name__ == "__main__":
    app.run(debug=True)


