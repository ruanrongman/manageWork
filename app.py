from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask import render_template
from models import query_user, User

app = Flask(__name__)

app.secret_key = 'fdfdfdsds'
app.config['MAIL_SERVER'] = 'xxx.xxxx.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录'
login_manager.session_protection = "strong"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user


@app.route('/')
@login_required
def index():
    print("weujwd")
    # return 'Logged in as: %s' % current_user.get_id()
    return render_template("gauge.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user_passwd = request.form['password']
        user = query_user(user_id)

        if user_id and user_passwd:
            print(user_id + user_passwd)
            if user:
                print("ewjfoooooooj" + user[1])
                if user[1] == user_passwd:
                    curr_user = User()
                    curr_user.id = user_id

                    # 通过Flask-Login的login_user方法登录用户
                    login_user(curr_user)

                    return redirect(url_for('index'))

                else:
                    flash('密码或用户名错误')
        else:
            flash("用户名和密码不能为空")
    # GET 请求
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1')
