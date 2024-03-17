from .extensions import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # country = db.Column(db.String(50), default='Ukraine')

    universities = db.relationship("University", back_populates="city")


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    city_id = db.Column(db.ForeignKey("city.id"))
    year_found = db.Column(db.Integer, nullable=True)

    city = db.relationship("City", back_populates="universities")
    courses = db.relationship("Course", back_populates="university")


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    university_id = db.Column(db.ForeignKey("university.id"))

    university = db.relationship("University", back_populates="courses")

