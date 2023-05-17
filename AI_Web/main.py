from flask import Flask, render_template,request, redirect,abort, send_from_directory
import pymysql.cursors
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,login_required,login_user,current_user,logout_user


login_manager= LoginManager()


app= Flask(__name__)
login_manager.init_app(app)

app.config['SECRET_KEY']='kjsbkjfgabfjknbrgojajovnajov'

class User:
    def __init__(self,id,user,banned):
        self.is_authenticated = True
        self.is_anonymous= False
        self.is_active = not banned

        self.username=user
        self.id=id
    
    def get_id(self):
        return str(self.id)


connection= pymysql.connect(
   
    host="10.100.33.60",
    user="mkhan",
    password='221085624',
    database='',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True

)

@login_manager.user_loader
def user_loader(user_id):
    cursor= connection.cursor()


@app.route("/")
def index(): 
    return render_template("index.html.jinja")



@app.route('/sign-in',methods=['GET'])
def sign_in():
    if request.method == 'POST':
        cursor= connection.cursor()
        cursor.execute('SELECT * FROM `users` WHERE `user` = %s',(request.form['username']))
        result= cursor.fetchone()


        if result is None:
            return redirect("/sign-in")
        
        if result['password'] == request.form['password']:
            user= User(result['id'],result['user'],result['ban'])

            login_user(user)

            return redirect('/feed')
        else:
            return render_template("sign_in.html.jinja")
        
    elif request.method=='GET':
        return render_template("sign_in.html.jinja")

        

    return render_template("sign_in.html.jinja")










if __name__=='__main__':
    app.run(debug=True)