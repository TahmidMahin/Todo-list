from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = '*************'


@app.before_request
def before_request():
    g.username = None
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
	return render_template('home.html', message=message)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		session.pop('username', None)
		username = request.form['username']
		password = request.form['password']
		if not model.find_user(username):
			message = "Username does not exist"
			return render_template('login.html', message=message)
		if password == model.get_password(username):
			session['username'] = username
			return redirect(url_for('home'))
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
    return redirect(url_for('home'))

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
	app.run(port = 6969, debug=True)