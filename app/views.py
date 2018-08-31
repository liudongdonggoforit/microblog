from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
	user = {'name':'Miguel'}
	posts = [{
		'author':{'name':'John'},
		'body':'Beautiful day in Portland!'
	},{
		'author':{'name':'Susan'},
		'body':'The Avengers movie was so cool!'
	}]
	return render_template("index.html",user = user,title = 'Home',posts = posts)

#这里唯一的新的知识点就是路由装饰器的 methods 参数。
#参数告诉 Flask 这个视图函数接受 GET 和 POST 请求。如果不带参数的话，视图只接受 GET 请求。
@app.route('/login',methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '",remember_me=' +str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
		title = 'Sigh In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])