from flask import request, flash, url_for, redirect, render_template
from forms import Registration, LogIn,AddVenue
from flask_login import login_user , logout_user , current_user , login_required, LoginManager
from config import app, db
from Models import Acc,User,Venue,Location,Room

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "You have logged out."
#separate as routes.py if linecount is great-----------------------------
@app.route("/")

@app.route("/index", methods=['GET','POST'])
def main():
    return render_template('index.html')

@app.route("/landing")
@login_required
def landing():
    return render_template('landing.html')

@app.route("/venue", methods=['GET'])
@login_required
def venue():
    return render_template('venue.html')

@app.route("/logout")
@login_required
def logout():
    flash('You have logged out!')
    logout_user()
    return redirect(url_for('main'))

@app.route("/register", methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        print form.username.data
        #if username/email is already used
        if Acc.query.filter_by(username=form.username.data).first():
            flash('Username already exists. Try a different username.')
            return redirect(url_for('register'))
        if Acc.query.filter_by(email=form.email.data).first():
            flash('Email already used. Use a different email address.')
            return redirect(url_for('register'))
        #if user,email does not exist yet, and passwords match, register.
        newacc = Acc(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(newacc)
        db.session.commit()
        #user is an account. so create account first before assigning user.
        user = User(Acc.get_id(newacc),form.fname.data, form.lname.data, '')
        db.session.add(user)
        db.session.commit()
        flash('Account created for Acc.username!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogIn(request.form)
    if form.validate_on_submit():
        #Does email exist in db?
        user = Acc.query.filter_by(email=form.email.data).first()
        if user:
            #Is pass correct?
            if user.password == form.password.data:
                #If email exists and pass is correct, login.
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('landing'))
        flash ('Invalid email or password.', 'error')
    return render_template('login.html', form=form)

@app.route("/addvenue", methods=['GET', 'POST'])
@login_required
def addvenue():
    form = AddVenue()
    if form.validate_on_submit():
        #If Location isn't filled up, use room name and college
        if form.location.data == '' or form.location.data == None:
            newvenue = Venue(capacity=form.capacity.data, rate=form.rate.data, equipment=form.equipment.data, venue_type='Room')
            db.session.add(newvenue)
            db.session.commit()
            venueroom = Room(id=Venue.get_id(newvenue), name=form.room.data, college=form.college.data)
            db.session.add(venueroom)
            db.session.commit()
        #If Location is filled up, use location instead
        elif form.location.data != '':
            newvenue = Venue(capacity=form.capacity.data, rate=form.rate.data, equipment=form.equipment.data, venue_type='Non-College Location')
            db.session.add(newvenue)
            db.session.commit()
            location = Location(id=Venue.get_id(newvenue), name=form.location.data)
            db.session.add(location)
            db.session.commit()
        flash('Venue created.')
        return redirect(url_for('venue'))
    return render_template('addvenue.html', form=form)
#separate as routes.py if linecount is great-----------------------------

@login_manager.user_loader
def load_user(acc_id):
    reg_user = Acc.query.filter_by(id=acc_id).first()
    #User.query.get(int(acc_id))
    return reg_user

if __name__ == "__main__":
    app.run(debug=True)


