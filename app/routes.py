from flask_restx import Resource, Namespace

from app import db
from app.api_models import city_model, city_input_model, university_model, university_input_model
from app.models import City, University

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {'Hello': "restx"}


@ns.route("/cities")
class CityListAPI(Resource):
    @ns.marshal_list_with(city_model)
    def get(self):
        return City.query.all()

    @ns.expect(city_input_model)
    @ns.marshal_with(city_model)
    def post(self):
        city = City(name=ns.payload["name"])
        db.session.add(city)
        db.session.commit()
        return city, 201

@ns.route("/cities/<int:id>")
class CityAPI(Resource):
    @ns.marshal_with(city_model)
    def get(self, id):
        city = City.query.get(id)
        return city


    @ns.expect(city_input_model)
    @ns.marshal_with(city_model)
    def put(self, id):
        city = City.query.get(id)
        city.name = ns.payload["name"]
        db.session.commit()
        return city
    #
    def delete(self, id):
        city = City.query.get(id)
        db.session.delete(city)
        db.session.commit()
        return {}, 204

# @ns.route("/courses/<int:id>")
# class CourseAPI(Resource):
#     @ns.marshal_with(city_model)
#     def get(self, id: int):
#         city = City.query.get(id)
#         return city



@ns.route("/universities")
class UniversityAPI(Resource):
    @ns.marshal_list_with(university_model)
    def get(self):
        return University.query.all()

    @ns.expect(university_input_model )
    @ns.marshal_with(university_model)
    def post(self):
        university = University(name=ns.payload["name"],
                          city_id=ns.payload["city_id"],
                          year_found=ns.payload["year_found"])
        db.session.add(university)
        db.session.commit()
        return university, 201
