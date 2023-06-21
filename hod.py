from flask import *
from database import *

hod=Blueprint('hod',__name__)

@hod.route('/hodhome',methods=['get','post'])
def hodhome():
	return render_template('hodhome.html')

@hod.route('/add_teacher',methods=['get','post'])
def add_teachers():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		sname=request.form['sname']
		fname=request.form['fname']
		lname=request.form['lname']
		qual=request.form['qual']
		gender=request.form['gender']
		email=request.form['email']
		phone=request.form['phone']
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(username,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','teacher')"%(username,password)
			res=insert(q)
			q="insert into teachers values(null,'%s',(select hod_id from hod where login_id='%s'),'%s','%s','%s','%s','%s','%s','%s')"%(res,ids,sname,fname,lname,qual,gender,email,phone)
			insert(q)
			flash("Registered Successfully")
	q="select * from subjects"
	res=select(q)
	data['sub']=res
	return render_template('hodadd_teachers.html',data=data)

@hod.route('/view_teachers',methods=['get','post'])
def view_teachers():
	data={}
	ids=session['login_id']
	q="select * from teachers inner join subjects using(subject_id) inner join courses using(course_id) inner join departments using(department_id) inner join college using(college_id) inner join hod using(hod_id) where hod.login_id='%s'"%(ids)
	res=select(q)
	data['teachers']=res
	return render_template('hodview_teachers.html',data=data)