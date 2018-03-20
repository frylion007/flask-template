from flask.views import MethodView
from flask import render_template,request

class Login(MethodView):
    @staticmethod
    def get(user_name):
        return render_template("admin/index.html",user_name=user_name)

    def post(self):
        pass


# as_view
LoginView = Login.as_view("Login")
