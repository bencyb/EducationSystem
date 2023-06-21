from flask import *
from database import *
import uuid
teacher=Blueprint('teacher',__name__)

@teacher.route('/teacherhome',methods=['get','post'])
def teacherhome():
	data={}
	ids=session['login_id']
	q="select * from teachers where login_id='%s'"%(ids)
	res=select(q)
	data['teach']=res
	return render_template('teacherhome.html',data=data)


@teacher.route('/manageassignments',methods=['get','post'])
def manageassignments():
	data={}
	ids=session['login_id']
	q="select * from teachers inner join subjects using(subject_id) where login_id='%s'"%(ids)
	res=select(q)
	data['updateprt']=res
	if 'submit' in request.form:
		title=request.form['title']
		des=request.form['des']
		assigndate=request.form['adate']
		lastday=request.form['ldate']
		maxmark=request.form['mark']
		q="insert into assignments values(null,(select teacher_id from teachers where login_id='%s'),'%s','%s','%s','%s','%s')"%(ids,title,des,assigndate,lastday,maxmark)
		insert(q)
		flash('Successfully Added')
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from assignments where assignment_id='%s'"%(id)
		delete(q)
		return redirect(url_for('teacher.manageassignments'))

	if action=="update":
		q="select * from assignments inner join teachers using(teacher_id) where assignment_id='%s'"%(id)
		res=select(q)
		data['updassign']=res

	if 'update' in request.form:
		title=request.form['title']
		des=request.form['des']
		assigndate=request.form['adate']
		lastday=request.form['ldate']
		maxmark=request.form['mark']
		q="update assignments set title='%s',description='%s',ass_date='%s',last_date_sub='%s',max_mark='%s' where assignment_id='%s'"%(title,des,assigndate,lastday,maxmark,id)
		update(q)
		return redirect(url_for('teacher.manageassignments'))

	q="select *,concat(firstname,' ',lastname)as NAME from assignments inner join teachers where login_id='%s'"%(ids)
	res=select(q)
	data['assign']=res
	return render_template('teachermanageassignments.html',data=data)


@teacher.route('/managetasks',methods=['get','post'])
def managetasks():
	data={}
	ids=session['login_id']
	q="select * from teachers inner join subjects using(subject_id) where login_id='%s'"%(ids)
	res=select(q)
	data['up']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from task where task_id='%s'"%(id)
		delete(q)
		return redirect(url_for('teacher.managetasks'))
	if action=="update":
		q="select * from task inner join teachers using(teacher_id) where task_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		title=request.form['title']
		des=request.form['des']
		sub_date=request.form['sub_date']
		q="update task set task_title='%s',task_des='%s',task_sub_date='%s' where task_id='%s'"%(title,des,sub_date,id)
		update(q)
		return redirect(url_for('teacher.managetasks'))
	if 'submit' in request.form:
		title=request.form['title']
		des=request.form['des']
		sub_date=request.form['sub_date']
		q="insert into task values(null,(select teacher_id from teachers where login_id='%s'),'%s','%s','%s')"%(ids,title,des,sub_date)
		insert(q)
	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM task INNER JOIN `teachers` USING(teacher_id)INNER JOIN `subjects` USING(subject_id) WHERE login_id='%s'"%(ids)
	res=select(q)
	data['ta']=res
	return render_template('teachermanagetasks.html',data=data)


@teacher.route('/managenotes',methods=['get','post'])
def managenotes():
	data={}
	ids=session['login_id']
	q="select * from teachers inner join subjects using(subject_id) where login_id='%s'"%(ids)
	res=select(q)
	data['up']=res
	if 'submit' in request.form:
		title=request.form['title']
		upload_file=request.files['upload_file']
		path='static/uploads/'+str(uuid.uuid4())+upload_file.filename
		upload_file.save(path)
		q="insert into note values(null,(select teacher_id from teachers where login_id='%s'),'%s','%s',Curdate())"%(ids,title,path)
		insert(q)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from note where note_id='%s'"%(id)
		delete(q)
		return redirect(url_for('teacher.managenotes'))

	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM `note` INNER JOIN `teachers` USING(teacher_id)INNER JOIN `subjects` USING(subject_id) WHERE login_id='%s'"%(ids)
	res=select(q)
	data['no']=res
	return render_template('teachermanagenotes.html',data=data)


@teacher.route('/managereviews',methods=['get','post'])
def managereviews():
	return render_template('teachermanagereviews.html')


@teacher.route('/viewcollegeprofile',methods=['get','post'])
def viewcollegeprofile():
	data={}
	q="select * from college"
	res=select(q)
	data['college']=res
	return render_template('teacherviewcollegeprofile.html',data=data)

# 
@teacher.route('/viewdepartments',methods=['get','post'])
def viewdepartments():
	data={}
	q="select * from departments"
	res=select(q)
	data['dep']=res
	return render_template('teacher_viewdepartments.html',data=data)


@teacher.route('/viewcourses',methods=['get','post'])
def viewcourses():
	data={}
	q="select * from courses inner join departments using(department_id)"
	res=select(q)
	data['course']=res
	return render_template('teacher_viewcourses.html',data=data)
	
@teacher.route('/viewallteachers',methods=['get','post'])
def viewallteachers():
	data={}
	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM `teachers` INNER JOIN  `subjects` USING(subject_id)INNER JOIN `courses` USING(course_id)"
	res=select(q)
	data['te']=res
	return render_template('teacherview_all.html',data=data)

@teacher.route('/view_course',methods=['get','post'])
def view_course():
	data={}
	q="select * from courses"
	res=select(q)
	data['co']=res
	return render_template('teacher_viewcourse.html',data=data)

@teacher.route('/viewstudents',methods=['get','post'])
def viewstudents():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from students inner join courses using(course_id)where course_id='%s'"%(id)
	res=select(q)
	data['st']=res
	return render_template('teacherviewstudents.html',data=data)


@teacher.route('/viewmessages',methods=['get','post'])
def viewmessages():
	data={}
	ids=session['login_id']
	q="select *,concat(students.firstname,' ',students.lastname)as NAME from messages inner join students using(student_id) inner join teachers using(teacher_id) where teachers.login_id='%s'"%(ids)
	res=select(q)
	data['messages']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE messages SET reply='%s' WHERE message_id='%s'" %(reply,res[j]['message_id'])
			update(q)
			flash("send message")
			return redirect(url_for('teacher.viewmessages'))
		j=j+1
	return render_template('teacher_viewmessages.html',data=data)

@teacher.route('/view_subjects',methods=['get','post'])
def view_subjects():
	data={}
	id=request.args['id']
	q="SELECT * FROM `subjects` INNER JOIN courses USING(course_id) where course_id='%s'"%(id)
	res=select(q)
	data['sub']=res
	return render_template('teacherview_subjects.html',data=data)

@teacher.route('/view_reviews',methods=['get','post'])
def view_reviews():
	data={}
	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM `feedback` INNER JOIN students USING(student_id)"
	res=select(q)
	data['re']=res
	return render_template('teacherview_reviews.html',data=data)

@teacher.route('/mark_attendence',methods=['get','post'])
def mark_attendence():
	id=request.args['id']
	ids=session['login_id']
	if 'submit' in request.form:
		status=request.form['attendence']
		q="insert into attendence values(null,(select teacher_id from teachers where login_id='%s'),'%s','%s',Curdate())"%(ids,id,status)
		insert(q)
	return render_template('teachersmark_attendence.html')

@teacher.route('/view_studentsubmission',methods=['get','post'])
def view_studentsubmission():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from stud_submission inner join students using(student_id)"
	res=select(q)
	data['sub']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			status=request.form['status'+str(i)]
			q="UPDATE stud_submission SET status='%s' WHERE submit_id='%s'" %(status,res[j]['submit_id'])
			update(q)
			flash("send message")
			return redirect(url_for('teacher.view_studentsubmission'))
		j=j+1
	return render_template('teacherview_studentsubmission.html',data=data)
