from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)


@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')


@admin.route('/add_collegedetails',methods=['get','post'])
def add_collegedetails():
	if 'submit' in request.form:
		cname=request.form['cname']
		image=request.files['img']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		desc=request.form['descr']
		address=request.form['address']
		email=request.form['email']
		phone=request.form['phone']
		
		q="select * from college where college_name='%s'" %(cname)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That College is already exist")
		else:
			q="insert into college values(null,'%s','%s','%s','%s','%s','%s')"%(cname,path,desc,address,email,phone)
			insert(q)
			flash("Registered Successfully")

	return render_template('adminadd_collegedetails.html')


@admin.route('/add_department',methods=['get','post'])
def add_department():
	data={}
	if 'submit' in request.form:
		cname=request.form['cname']
		dname=request.form['dname']
		desc=request.form['desc']
		q="select * from departments where dep_name='%s'" %(dname)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That department is already exist")
		else:
			q="insert into departments values(null,'%s','%s','%s')"%(cname,dname,desc)
			insert(q)
			flash("Added Successfully")
	q="select * from college"
	res=select(q)
	data['co']=res
	return render_template('adminadd_department.html',data=data)


@admin.route('/add_course',methods=['get','post'])
def add_course():
	data={}
	if 'submit' in request.form:
		dname=request.form['dname']
		cname=request.form['cname']
		des=request.form['des']
		q="insert into courses values(null,'%s','%s','%s')"%(dname,cname,des)
		insert(q)
		flash("Course Added..")
	q="select * from departments"
	res=select(q)
	data['dep']=res
	return render_template('adminadd_course.html',data=data)
	

@admin.route('/add_subject',methods=['get','post'])
def add_subject():
	data={}
	if 'submit' in request.form:
		cname=request.form['cname']
		sname=request.form['subname']
		des=request.form['desc']
		q="insert into subjects values(null,'%s','%s','%s')"%(cname,sname,des)
		insert(q)
		flash("Subject Added..")
	q="select * from courses"
	res=select(q)
	data['courses']=res
	return render_template('adminadd_subject.html',data=data)


@admin.route('/add_teacher',methods=['get','post'])
def add_teachers():
	data={}
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
			q="insert into teachers values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,sname,fname,lname,qual,gender,email,phone)
			insert(q)
			flash("Registered Successfully")
	q="select * from subjects"
	res=select(q)
	data['sub']=res
	return render_template('adminadd_teachers.html',data=data)


@admin.route('/view_collegedetails',methods=['get','post'])
def view_collegedetails():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from college where college_id='%s'"%(id)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('admin.view_collegedetails'))
	if action=="update":
		q="select * from college where college_id='%s'"%(id)
		res=select(q)
		data['updatecollege']=res
	
	if 'update' in request.form:
		cname=request.form['cname']
		image=request.files['img']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		desc=request.form['descr']
		address=request.form['address']
		email=request.form['email']
		phone=request.form['phone']
		q="update college set college_name='%s',image='%s',description='%s',address='%s',email='%s',phone='%s' where college_id='%s'"%(cname,path,desc,address,email,phone,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('admin.view_collegedetails'))
	q="select * from college"
	res=select(q)
	data['college']=res
	return render_template('adminview_collegedetails.html',data=data)

@admin.route('/view_departments',methods=['get','post'])
def view_departments():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from departments where department_id='%s'"%(id)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('admin.view_departments'))
	if action=="update":
		q="select * from departments inner join college using(college_id) where department_id='%s'"%(id)
		res=select(q)
		data['updatedepartments']=res
	if 'update' in request.form:
		dname=request.form['dname']
		des=request.form['des']
		q="update departments set dep_name='%s',dep_description='%s' where department_id='%s'"%(dname,des,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('admin.view_departments'))
	q="select * from departments inner join college using(college_id)"
	res=select(q)
	data['departments']=res
	return render_template('adminview_department.html',data=data)


@admin.route('/view_course',methods=['get','post'])
def view_course():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from courses where course_id='%s'"%(id)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('admin.view_course'))
	if action=="update":
		q="select * from courses inner join departments using(department_id) where course_id='%s'"%(id)
		res=select(q)
		data['updatecourses']=res
	if 'update' in request.form:
		cname=request.form['cname']
		des=request.form['des']
		q="update courses set course_title='%s',description='%s' where course_id='%s'"%(cname,des,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('admin.view_course'))
	q="select * from courses inner join departments using(department_id)"
	res=select(q)
	data['courses']=res
	return render_template('adminview_course.html',data=data)


@admin.route('/view_subjects',methods=['get','post'])
def view_subjects():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from subjects where subject_id='%s'"%(id)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('admin.view_subjects'))
	if action=="update":
		q="select * from subjects inner join courses using(course_id) where subject_id='%s'"%(id)
		res=select(q)
		data['updatesubjects']=res
	if 'update' in request.form:
		cname=request.form['cname']
		des=request.form['des']
		q="update subjects set sub_name='%s',sub_description='%s' where subject_id='%s'"%(cname,des,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('admin.view_subjects'))
	q="select * from subjects inner join courses using(course_id)"
	res=select(q)
	data['subjects']=res
	return render_template('adminview_subject.html',data=data)


@admin.route('/view_teacher',methods=['get','post'])
def view_teacher():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="update":
		q="select * from teachers where teacher_id='%s'"%(id)
		res=select(q)
		data['upd']=res
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		qual=request.form['qual']
		gender=request.form['gender']
		email=request.form['email']
		phone=request.form['phone']
		q="update teachers set firstname='%s',lastname='%s',qualification='%s',gender='%s',email='%s',phone='%s' where teacher_id='%s'"%(fname,lname,qual,gender,email,phone,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('admin.view_teacher'))
	q="select * from teachers"
	res=select(q)
	data['teacher']=res
	return render_template('adminview_teacher.html',data=data)


@admin.route('/view_allteachers',methods=['get','post'])
def view_allteachers():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from teachers where teacher_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('admin.view_allteachers'))
	q="select * from teachers inner join subjects using(subject_id) inner join courses using(course_id) inner join departments using(department_id) inner join college using(college_id)"
	res=select(q)
	data['teachers']=res
	return render_template('adminview_allteachers.html',data=data)


@admin.route('/view_students',methods=['get','post'])
def view_students():
	data={}
	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM `students` INNER JOIN `courses` USING(course_id) inner join login using(login_id)"
	res=select(q)
	data['st']=res
	if 'id1' in request.args:
		id1=request.args['id1']
		q="update login set  usertype='Student'  where login_id='%s' and usertype='pending'"%(id1)
		update(q)
		return redirect(url_for('admin.view_students'))
	elif 'id2' in request.args:
		id2=request.args['id2']
		q="update login set  usertype='Rejected'  where login_id='%s' and usertype='pending'"%(id2)
		update(q)
		return redirect(url_for('admin.view_students'))
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id3=request.args['id3']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id3)
		delete(q)
		q="delete from students where student_id='%s'"%(id)
		delete(q)
		flash("Removed from Our List...")
	return render_template('adminview_students.html',data=data)


@admin.route('/view_feedbacks',methods=['get','post'])
def view_feedbacks():
	data={}
	q="SELECT *,CONCAT(firstname,' ',lastname)AS NAME FROM feedback INNER JOIN students USING(student_id)"
	res=select(q)
	data['fe']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" %(reply,res[j]['feedback_id'])
			update(q)
			flash("send message")
			return redirect(url_for('admin.view_feedbacks'))
		j=j+1
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from feedback where feedback_id='%s'"%(feedback_id)
		delete(q)
		flash("Deleted from Our System...")
	return render_template('adminview_feedbacks.html',data=data)

@admin.route('/send_notification',methods=['get','post'])
def send_notification():
	if 'submit' in request.form:
		note=request.form['note']
		q="insert into notification values(null,'%s',Curdate())"%(note)
		insert(q)
		flash("Notification Added..")
	return render_template('adminsend_notification.html')

@admin.route('/add_fee',methods=['get','post'])
def add_fee():
	data={}
	if 'submit' in request.form:
		cname=request.form['cname']
		fee=request.form['fee']
		duration=request.form['duration']
		sem=request.form['sem']
		total_amount=int(fee)*int(sem)
		q="insert into fee values(null,'%s','%s','%s','%s','%s')"%(cname,fee,duration,sem,total_amount)
		insert(q)
	q="select * from courses"
	res=select(q)
	data['courses']=res
	return render_template('adminadd_fee.html',data=data)

@admin.route('/view_notification',methods=['get','post'])
def view_notification():
	data={}
	q="select * from notification"
	res=select(q)
	data['no']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from notification where note_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.view_notification'))
	return render_template('adminview_notification.html',data=data)

@admin.route('/view_fee',methods=['get','post'])
def view_fee():
	data={}
	q="select * from fee inner join courses using(course_id)"
	res=select(q)
	data['fe']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from fee where fee_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.view_fee'))
	return render_template('adminview_fee.html',data=data)

@admin.route('/conduct_exam',methods=['get','post'])
def conduct_exam():
	data={}
	q="select * from courses"
	res=select(q)
	data['co']=res
	if 'submit' in request.form:
		cname=request.form['cname']
		etitle=request.form['etitle']
		sdate=request.form['sdate']
		edate=request.form['edate']
		edes=request.form['edes']
		etype=request.form['type']
		q="insert into exam values(null,'%s','%s','%s','%s','%s','%s','pending')"%(cname,etitle,sdate,edate,edes,etype)
		insert(q)
	return render_template('adminconduct_exam.html',data=data)

@admin.route('/view_exam_details',methods=['get','post'])
def view_exam_details():
	data={}
	q="select * from exam inner join courses using(course_id)"
	res=select(q)
	data['ex']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from exam where exam_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.view_exam_details'))
	return render_template('adminview_exam_details.html',data=data)

@admin.route('/manage_payment',methods=['get','post'])
def manage_payment():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from payment  inner join students using(student_id)inner join courses on students.course_id=courses.course_id"
	res=select(q)
	data['pay']=res
	if 'id' in request.args:
		id=request.args['id']
		q="update payment set  pay_status='Payment Accept'  where payment_id='%s' and pay_status='Paid'"%(id)
		update(q)
		return redirect(url_for('admin.manage_payment'))
	elif 'id1' in request.args:
		id1=request.args['id1']
		q="update payment set  pay_status='Payment Reject'  where payment_id='%s' and pay_status='Paid'"%(id1)
		update(q)
		return redirect(url_for('admin.manage_payment'))
	return render_template('adminmanage_payment.html',data=data)

@admin.route('/add_hod',methods=['get','post'])
def add_hod():
	data={}
	id=request.args['id']
	q="select * from departments where department_id='%s'"%(id)
	res=select(q)
	data['dep']=res
	if 'submit' in request.form:
		name=request.form['name']
		address=request.form['address']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(username,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','HOD')"%(username,password)
			res=insert(q)
			q="insert into hod values(null,'%s','%s','%s','%s','%s','%s')"%(res,id,name,address,phone,email)
			insert(q)
			return redirect(url_for('admin.view_departments'))
	return render_template('adminadd_hod.html',data=data)

@admin.route('/view_hod',methods=['get','post'])
def view_hod():
	data={}
	q="select * from hod inner join departments using(department_id)"
	res=select(q)
	data['ho']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from hod where hod_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.view_hod'))
	if action=="update":
		q="select * from hod inner join departments using(department_id)"
		res=select(q)
		data['updateprte']=res
	if 'update' in request.form:
		name=request.form['name']
		address=request.form['address']
		phone=request.form['phone']
		email=request.form['email']
		q="update hod set hod_name='%s',hod_address='%s',hod_phone='%s',hode_email='%s' where hod_id='%s'"%(name,address,phone,email,id)
		update(q)
		return redirect(url_for('admin.view_hod'))
	return render_template('adminview_hod.html',data=data)
