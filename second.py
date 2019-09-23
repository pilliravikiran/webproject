from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/home')
def index():
	return "<h1>TejaDvv Kalyan Teja</h1>"
'''@app.route('/index/<name>')
def index1(name):
	return "<h1>This is index page <br> we can't give same url for many functions</h1>"+name'''
@app.route('/index/<int:age>')
def index2(age):
	#return "{}".format(age)
	return "%d" %age
@app.route('/index/<float:age>')
def index3(age):
	return "%f" %age
#Function Mapping
@app.route('/pic/admin')
def admin():
			return "this is admin"
@app.route('/pic/student')
def student():
			return "this is student"
@app.route('/index/<str>')
def index4(str):
	if(str =="admin"):
		#return admin()
		return redirect(url_for('admin'))
	if(str =="student"):
		#return student()
		return redirect(url_for('student'))
	else :
		return "Nope"
#Login Page
'''@app.route('/login/<name>')
def login(name):
	return render_template('login.html',username=name)'''
@app.route('/login/<int:val>')
def login1(val):
	return render_template('login.html',value=val)
#File Uploading
@app.route('/upload')
def upload():
	return render_template('upload.html')
@app.route('/success',methods=['POST','GET'])
def success():
	if request.method=='POST':
		f=request.files['file']
		f.save(f.filename)
		return render_template('success.html',fname=f.filename)

if __name__=='__main__':
	app.run(debug=True)