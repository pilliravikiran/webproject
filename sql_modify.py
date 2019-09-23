from flask import *
from flask_mail import Mail,Message
from db import Register,Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager,current_user,login_user,logout_user,login_required


app= Flask(__name__)

login_manager=LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
	return session.query(User).get(int(user_id))

engine = create_engine('sqlite:///regiter.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind =engine
DBsession =sessionmaker(bind=engine)
session =DBsession()
app.secret_key='teja'

@app.route('/show')
def showData():
	data=session.query(Register).all()
	return render_template('show.html',data=data)

@app.route('/add',methods=['POST','GET'])
def add_data():
	if request.method=='POST':
		newData=Register(name=request.form['name'],
			email=request.form['email'],
			pwd=request.form['pwd'],
			des=request.form['des'])
		session.add(newData)
		session.commit()
		flash("New Data is Added")
		return redirect(url_for('showData'))
	else:
		return render_template('add_data.html')


@app.route('/edit/<int:register_id>',methods=['POST','GET'])
def edit_data(register_id):
	editeddata=session.query(Register).filter_by(id=register_id).one()
	if request.method=='POST':
		editeddata.name=request.form['name']
		editeddata.email=request.form['email']
		editeddata.pwd=request.form['pwd']
		editeddata.des=request.form['des']
		session.add(editeddata)
		session.commit()
		flash(str(register_id)+ " record is Edited")
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editeddata)


@app.route('/delete/<int:del_id>')
def delete(del_id):
	delrecord = session.query(Register).filter_by(id=del_id).one()
	session.delete(delrecord)
	session.commit()
	flash(str(del_id)+ " record is Deleted")
	return redirect(url_for('showData'))

@app.route('/register',methods=['POST','GET'])
def register_Data():
	if request.method=='POST':
		logindata=User(email=request.form['email'],
						pwd=request.form['pwd'])
		session.add(logindata)
		session.commit()
		return redirect(url_for('login'))
	else:
		return render_template('register.html')

@app.route('/login',methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('showData'))
	try:
		if request.method=='POST':
			user =session.query(User).filter_by(
				email=request.form['email'],
				pwd=request.form['pwd']).first()
			if user:
				login_user(user)
				return redirect(url_for('showData'))
			else:
				flash("Login failed")
		else:
			return render_template('login1.html',title='login')
	except Exception as e:
		flash("Login failed")
	else:
		return render_template('login1.html',title='login')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('showData'))



if(__name__)=='__main__':
	app.run(debug=True)