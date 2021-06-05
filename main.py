from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = **********

@app.before_request
def before_request():
    g.username = None
    g.admin = None
    if 'admin' in session:
    	g.admin = session['admin']
    if 'username' in session:
        g.username = session['username']

@app.route('/', methods = ['GET', 'POST'])
def home():
	if 'username' in session:
		g.user = session['username']
		username = session['username']
		if request.method == 'GET':
			query = model.get_activity(username)
			return render_template('dashboard.html', query=query)
		else:
			if request.form['action'] == 'add':
				activity = request.form['activity']
				status = request.form['status']
				model.add_activity(username, activity, status)
			elif request.form['action'] == 'remove':
				activity = request.form['activity']
				model.remove_activity(username, activity)
			elif request.form['action'] == 'update':
				activity = request.form['activity']
				status = request.form['status']
				model.update_activity(username, activity, status)

			return redirect(url_for('home'))

	message = "Login or signup"
	session.pop('admin', None)
	return render_template('home.html', message=message)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	message = ""
	if request.method == 'POST':
		session.pop('username', None)
		session.pop('admin', None)
		username = request.form['username']
		password = request.form['password']
		if not model.find_user(username):
			message = "Username does not exist"
			return render_template('login.html', message=message)
		if password == model.get_password(username):
			session['username'] = username
			return redirect(url_for('home'))
		else:
			message = "Incorrect password"
	return render_template('login.html', message=message)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		message = "Sign up here"
		return render_template('signup.html', message=message)

	username = request.form["username"]
	password = request.form["password"]
	confirm_pass = request.form["confirmpassword"]
	if model.find_user(username):
		message = "This username already exists!"
		return render_template('signup.html', message=message)
	if password != confirm_pass:
		message = "Passwords don't match"
		return render_template('signup.html', message=message)
	if len(password) < 6:
		message = "Password too short"
		return render_template('signup.html', message=message)
	model.add_user(username, password)
	message = "Account successfully created. Go login!"
	return render_template('signup.html', message=message)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('admin', None)
    return redirect(url_for('home'))

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
	if 'admin' not in session:
		message = ""
		if request.method == 'POST':
			session.pop('username', None)
			session.pop('admin', None)
			admin = request.form['admin']
			password = request.form['password']
			if not model.find_admin(admin):
				message = "Admin does not exist"
				return render_template('admin.html', message=message)
			if password == model.get_admin_password(admin):
				session['admin'] = admin
				return redirect(url_for('admin'))
			else:
				message = "Incorrect password"
		return render_template('admin.html', message=message)
	g.admin = session['admin']
	admin = session['admin']
	totalUser = str(model.get_totalUser())
	newUser = str(model.get_newUser())
	totalList = str(model.get_totalList())
	return render_template('admindash.html', totalUser=totalUser, newUser=newUser, totalList=totalList)

@app.route('/admin/users', methods = ['GET', 'POST'])
def adminUser():
	query = []
	if request.method == 'GET':
		users = model.get_users()
		return render_template('adminUser.html', users=users, query=query)
	if request.form['action'] == 'remove':
		username = request.form['user']
		model.remove_user(username)
	elif request.form['action'] == 'show activity':
		username = request.form['user']
		query = mode.get_activity(username)
	return redirect(url_for('adminUser'))


@app.route('/about-us', methods = ['GET'])
def aboutus():
	return render_template('aboutus.html')

@app.route('/terms-of-use', methods = ['GET'])
def termsofuse():
	return render_template('termsofuse.html')

@app.route('/privacy', methods = ['GET'])
def next():
	return render_template('privacy.html')

if __name__ == '__main__':
	app.run(port = 4200, debug=True)
