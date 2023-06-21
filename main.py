from flask import Flask
from public import public
from admin import admin
from teacher import teacher
from student import student
from hod import hod
app=Flask(__name__)
app.secret_key="OIE"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(teacher,url_prefix='/teacher')
app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(hod,url_prefix='/hod')
app.run(debug=True,port=5085)










