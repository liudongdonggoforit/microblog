#python 2 from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

#我相信这个类不言而明。我们导入 Form 类，接着导入两个我们需要的字段类，TextField 和 BooleanField。
#DataRequired 验证器只是简单地检查相应域提交的数据是否是空。在 Flask-WTF 中有许多的验证器，
#我们将会在以后看到它们。
class LoginForm(Form):
	openid = StringField('openid',validators =[DataRequired()])
	remember_me = BooleanField('remember_me', default = False)