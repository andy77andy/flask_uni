

from .extensions import api
from flask_restx import fields


university_model = api.model("University", {
    "id": fields.Integer,
    "name": fields.String,
    "city_id": fields.Integer,
    "year_found": fields.Integer,
})

city_model = api.model("City", {
    "id": fields.Integer,
    "name": fields.String,
    # "country": fields.String,
    "universities": fields.List(fields.Nested(university_model))
})

city_input_model = api.model("CityInput", {
    "name": fields.String,
})


course_model = api.model("City", {
    "id": fields.Integer,
    "name": fields.String,
    "university_id": fields.String,
})


university_input_model = api.model("UniversityInput", {
    "name": fields.String,
    "city_id": fields.Integer,
    "year_found": fields.Integer,
})


course_input_model = api.model("CityInput", {
    "name": fields.String,
    "university_id": fields.Integer,
})
