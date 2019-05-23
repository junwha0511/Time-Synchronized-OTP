from flask import Flask, g
from flask import Flask, flash, redirect, render_template, request, session, abort
import time #시간 api import
import hashlib
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('button.html')

@app.before_request
def before_request():
	hashSHA = hashlib.md5() 

	#UID 할당
	userNum = "001"
    
	#연도+날짜+시간
	t = time.strftime("%Y%m%d%M",time.gmtime(time.time()))  

	#9자리 고유키
	key = userNum+t

	result = key

	hashSHA.update(key.encode())

	for i in range(9):
	 	hashSHA.update(hashSHA.hexdigest().encode())
	g.hash = hashSHA.hexdigest()[0:7]

	

@app.route('/get', methods=['GET'])
def getOTPNumber():
    return render_template("otp.html", hash = g.hash)
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000)