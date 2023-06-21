from flask import *
from database import *
import uuid
student=Blueprint('student',__name__)

@student.route('/studenthome',methods=['get','post'])
def studenthome():
	data={}
	ids=session['login_id']
	q="select * from students where login_id='%s'"%(ids)
	res=select(q)
	data['stud']=res
	return render_template('studenthome.html',data=data)


@student.route('/sendfeedback',methods=['get','post'])
def sendfeedback():
	ids=session['login_id']
	if 'submit' in request.form:
		feed=request.form['feed']
		q="insert into feedback values(null,(select student_id from students where login_id='%s'),'%s','pending',Curdate())"%(ids,feed)
		insert(q)
		flash("Send Feedback")
	return render_template('student_sendfeedback.html')


@student.route('/viewcollegeprofile',methods=['get','post'])
def viewcollegeprofile():
	data={}
	q="select * from college"
	res=select(q)
	data['college']=res
	return render_template('studentview_collegeprofile.html',data=data)


@student.route('/viewdepartments',methods=['get','post'])
def viewdepartments():
	data={}
	q="select * from departments"
	res=select(q)
	data['dep']=res
	return render_template('student_viewdepartments.html',data=data)


@student.route('/viewcourses',methods=['get','post'])
def viewcourses():
	data={}
	q="select * from courses inner join departments using(department_id)"
	res=select(q)
	data['course']=res
	return render_template('student_viewcourses.html',data=data)


@student.route('/view_subjects',methods=['get','post'])
def view_subjects():
	data={}
	q="select * from subjects inner join courses using(course_id)"
	res=select(q)
	data['sub']=res
	return render_template('student_view_subjects.html',data=data)


@student.route('/viewallteachers',methods=['get','post'])
def viewallteachers():
	data={}
	q="select * from teachers inner join subjects using(subject_id) inner join courses using(course_id) inner join departments using(department_id)"
	res=select(q)
	data['teach']=res
	return render_template('studentview_allteachers.html',data=data)


@student.route('/view_profile',methods=['get','post'])
def view_profile():
	data={}
	ids=session['login_id']
	q="select *,concat(firstname,' ',lastname)as NAME from students inner join courses using(course_id) where login_id='%s'"%(ids)
	res=select(q)
	data['my']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="update":
		q="select * from students inner join courses using(course_id) where student_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		address=request.form['address']
		dob=request.form['dob']
		email=request.form['email']
		phone=request.form['phone']
		q="update students set firstname='%s',lastname='%s',address='%s',dob='%s',email='%s',phone='%s' where student_id='%s'"%(firstname,lastname,address,dob,email,phone,id)
		update(q)
		return redirect(url_for('student.view_profile'))
	return render_template('studentview_profile.html',data=data)
 

@student.route('/viewnotification',methods=['get','post'])
def viewnotification():
	data={}
	q="select * from notification"
	res=select(q)
	data['not']=res
	return render_template('studentview_notification.html',data=data)


@student.route('/viewteachers',methods=['get','post'])
def viewteachers():
	data={}
	q="select * from teachers inner join subjects using(subject_id) inner join courses using(course_id) inner join departments using(department_id) inner join college using(college_id)"
	res=select(q)
	data['teachers']=res
	return render_template('studentview_teachers.html',data=data)



@student.route('/sendmessages',methods=['get','post'])
def sendmessages():
	data={}
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		message=request.form['message']
		q="insert into messages values(null,(select student_id from students where login_id='%s'),'%s','%s','pending',curdate())"%(ids,id,message)
		insert(q)
	return render_template('studentsend_messages.html',data=data)

@student.route('/view_examdetails',methods=['get','post'])
def view_examdetails():
	data={}
	q="SELECT * FROM exam INNER JOIN courses USING(course_id)"
	res=select(q)
	data['ex']=res
	return render_template('studentview_examdetails.html',data=data)

@student.route('/view_mycourse',methods=['get','post'])
def view_mycourse():
	ids=session['login_id']
	data={}
	q="select * from students inner join courses using(course_id) where login_id='%s'"%(ids)
	res=select(q)
	data['co']=res
	return render_template('student_viewmycourse.html',data=data)

@student.route('/student_view',methods=['get','post'])
def student_view():
	data={}
	id=request.args['id']
	q="select * from courses where course_id='%s'"%(id)
	res=select(q)
	data['view']=res
	return render_template('studview_all_ass.html',data=data)


@student.route('/view_assignment',methods=['get','post'])
def view_assignment():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from assignments inner join teachers using(teacher_id) inner join subjects using(subject_id)inner join courses using(course_id)where course_id='%s'"%(id)
	res=select(q)
	data['as']=res
	return render_template('studentview_assignment.html',data=data)

@student.route('/view_task',methods=['get','post'])
def view_task():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from task inner join teachers using(teacher_id) inner join subjects using(subject_id)inner join courses using(course_id)where course_id='%s'"%(id)
	res=select(q)
	data['ta']=res
	return render_template('studentview_task.html',data=data)

@student.route('/view_notes',methods=['get','post'])
def view_notes():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from note inner join teachers using(teacher_id) inner join subjects using(subject_id)inner join courses using(course_id)where course_id='%s'"%(id)
	res=select(q)
	data['no']=res
	return render_template('studentview_note.html',data=data)

@student.route('/submit_assignment',methods=['get','post'])
def submit_assignment():
	data={}
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		file=request.files['files']
		path='static/uploads1/'+str(uuid.uuid4())+file.filename
		file.save(path)
		q="insert into stud_submission values(null,(select student_id from students where login_id='%s'),'%s','%s','Submitted',Curdate(),'Assignment')"%(ids,id,path)
		insert(q)
	return render_template('studentsubmit_assignment.html',data=data)

@student.route('/assignment_status',methods=['get','post'])
def assignment_status():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from stud_submission inner join students using(student_id) where login_id='%s' and type='Assignment' and type_id=(select assignment_id from assignments where assignment_id='%s')"%(ids,id)
	res=select(q)
	data['as']=res
	return render_template('student_assignsubmission.html',data=data)

@student.route('/submit_task',methods=['get','post'])
def submit_task():
	data={}
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		file=request.files['files']
		path='static/uploads1/'+str(uuid.uuid4())+file.filename
		file.save(path)
		q="insert into stud_submission values(null,(select student_id from students where login_id='%s'),'%s','%s','Submitted',Curdate(),'Task')"%(ids,id,path)
		insert(q)
	return render_template('studentsubmit_task.html',data=data)
@student.route('/task_status',methods=['get','post'])
def task_status():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from stud_submission inner join students using(student_id) where login_id='%s' and type='Task' and type_id=(select task_id from task where task_id='%s')"%(ids,id)
	res=select(q)
	data['as']=res
	return render_template('student_tasksubmission.html',data=data)

@student.route('/view_attendence',methods=['get','post'])
def view_attendence():
	data={}
	ids=session['login_id']
	q="select *,concat(firstname,' ',lastname)as NAME from attendence inner join students using(student_id) where login_id='%s'"%(ids)
	res=select(q)
	data['at']=res
	return render_template('studentview_attendence.html',data=data)


@student.route('/manage_fee',methods=['get','post'])
def manage_fee():
	data={}
	ids=session['login_id']
	q="select * from students inner join courses using(course_id) where login_id='%s'"%(ids)
	res=select(q)
	data['fe']=res
	return render_template('studentmanage_fee.html',data=data)

@student.route('/pay_fee',methods=['get','post'])
def pay_fee():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select * from fee inner join courses using(course_id) where course_id='%s'"%(id)
	res=select(q)
	data['pay']=res
	if 'submit' in request.form:
		q="insert into payment values(null,'%s',(select student_id from students where login_id='%s'),'Paid',Curdate())"%(id,ids)
		insert(q)
		return redirect(url_for('student.studenthome'))
	return render_template('studentpay_fee.html',data=data)



# @student.route('/pay_fee',methods=['get','post'])
# def pay_fee():
# 	data={}
# 	id=request.args['id']
# 	ids=session['login_id']
# 	if 'submit' in request.form:
# 		q="select * from booking where booking_id='%s'" %(id)
# 		result=select(q)
# 		if len(result)>0:
# 			flash("You are paid for this property")
# 		else:
# 			q="UPDATE `booking` SET status='Paid' WHERE status='Accept'"
# 			update(q)
# 			flash("Pay successfully")
# 		return redirect(url_for('user.booking_status'))
# 	# else:
# 	# 	flash("Payment failed")	
# 	id=request.args['id']	
# 	q="select * from fee inner join courses using(course_id) where course_id='%s'"%(id)
# 	res=select(q)
# 	data['pay']=res
# 	return render_template('studentpay_fee.html',data=data)

