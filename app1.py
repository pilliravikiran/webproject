from flask import Flask,render_template,request
from flask_mail import Mail, Message
from random import randint

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.hushmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dvvteja@hushmail.com'
app.config['MAIL_PASSWORD'] = 'krishnateja77'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
otp=randint(000000,999999)
@app.route("/")
def index():
   msg = Message('OTP Verfication', sender = 'dvvteja@hushmail.com', recipients = ['viyok@rev-mail.net'])
   msg.body = "<b>OTP:%d</b>"%otp
   mail.send(msg)
   return render_template('validate.html')

@app.route('/validation',methods=['POST','GET'])
def validation():
 	user_otp=request.form['user_otp']
 	if otp==int(user_otp):
 		return "Verfication Done"
 	else:
 		return "Verfication Failed"

if __name__ == '__main__':
   app.run(debug = True)