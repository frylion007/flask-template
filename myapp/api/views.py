from flask.views import MethodView
from flask import jsonify,request
from config import config

class TestApi(MethodView):
    @staticmethod
    def get(user_name):
        data = {}
        data["user_name"] = user_name
        data["version"] = config.VERSION
        return jsonify(data)

    def post(self):
        pass


# as_view
TestApiView = TestApi.as_view("TestApi")
