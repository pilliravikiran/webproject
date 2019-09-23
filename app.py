from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)

#app.config['DEBUG']=True
#app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']='dvvteja@gmail.com'
app.config['MAIL_PASSWORD']='krishnateja777'
#app.config['MAIL_DEFAULT_SENDER']='dvvteja@gmail.com'
#app.config['MAIL_MAX_EMAILS']=None
#app.config['MAIL_ASCII_ATTACHMENTS']=False

mail=Mail(app)
@app.route('/')
def index():
	msg=Message("Hi TejaDvv",recipients=['ksatish8886@gmail.com'])
	msg.body="Body of the Mail"
	#msg.html="<b>Body of the Mail</b>"
	mail.send(msg)
	return "Message sent successfully"

if __name__=='__main__':
	app.run(debug=True)

