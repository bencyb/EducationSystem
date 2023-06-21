from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pas=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,pas)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']	
			if res[0]['usertype']=="admin":
				flash("Login Successfully")
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="Student":
				flash("Login Successfully")
				return redirect(url_for('student.studenthome'))
			if res[0]['usertype']=="teacher":
				flash("Login Successfully")
				return redirect(url_for('teacher.teacherhome'))
			if res[0]['usertype']=="HOD":
				flash("Login Successfully")
				return redirect(url_for('hod.hodhome'))
		else:
			flash("invalid username and password")
	return render_template("login.html")

@public.route('/register',methods=['get','post'])
def register():
	data={}
	if 'submit' in request.form:
		cname=request.form['cname']
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		dob=request.form['dob']
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
			q="insert into login values(null,'%s','%s','pending')"%(username,password)
			res=insert(q)
			q="insert into students values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,cname,fname,lname,address,dob,email,phone)
			insert(q)
			flash("Registered Successfully")
	q="select * from courses"
	res=select(q)
	data['co']=res
	return render_template('register.html',data=data)