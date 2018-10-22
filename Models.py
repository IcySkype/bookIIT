from config import db

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

class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column('venue_id', db.Integer , primary_key=True)
    capacity = db.Column('capacity', db.Integer())
    rate = db.Column('rate', db.Integer)
    equipment = db.Column('equipment', db.String())
    venue_type = db.Column('venue_type', db.String())

    def __init__(self, capacity, rate, equipment,venue_type):
        self.capacity = capacity
        self.rate = rate
        self.equipment = equipment
        self.venue_type = venue_type
    def get_id(self):
        return unicode(self.id)

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column('location_id', db.Integer , primary_key=True)
    name = db.Column('location_name', db.String())

    def __init__(self,id, name):
        self.id = id
        self.name = name

class Room(db.Model):
    __tablename__ = "room"
    id = db.Column('room_id', db.Integer , primary_key=True)
    name = db.Column('room_name', db.String())
    college = db.Column('college', db.String())

    def __init__(self, id, name, college):
        self.id = id
        self.name = name
        self.college = college

