from flask import Flask, render_template,request, redirect,abort, send_from_directory, g
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

@login_manager.user_loader
def user_loader(user_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM `users` WHERE `id` = " + user_id)
    result = cursor.fetchone()
    if result is None:
        return None

    return User(result['id'], result['username'], result['pfp'], result['banned'])

def connect_db():
    return pymysql.connect(
    host="10.100.33.60",
    user="mkhan",
    password='221085624',
    database='mkhan_AI-WEB',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
    )

def get_db():
    '''Opens a new database connection per request.'''        
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db    

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''    
    if hasattr(g, 'db'):
        g.db.close() 

app.get('/media/<path:path>')
def send_media(path):
    return send_from_directory('media', path)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html.jinja'), 404

@app.route("/")
def index(): 
    return render_template("index.html.jinja")

@app.route('/sign-in',methods=['POST','GET'])
def sign_in():
    if request.method == 'POST':
        cursor= get_db().cursor()
        cursor.execute('SELECT * FROM `Users` WHERE `Username` = %s',(request.form['Username']))
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


@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        cursor = get_db().cursor()


        cursor.execute("""
            INSERT INTO `users` (`Username`, `Email`, `Password`) VALUES (%s, %s, %s)
        """, (request.form['Username'], request.form['Password'], request.form['Email']))
   
        cursor.close()
        return redirect('/')
    elif request.method == 'GET':
        return render_template("signup.html.jinja")




if __name__=='__main__':
    app.run(debug=True)