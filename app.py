from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

ADMIN_ID = "admin"
ADMIN_PASS = "1234"

# 👉 Login Page
@app.route('/')
def home():
    return render_template("login.html")

# 👉 Login Logic
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == ADMIN_ID and password == ADMIN_PASS:
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Wrong ID Password ❌"

# 👉 Dashboard (tera index.html)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("index.html")
    else:
        return redirect(url_for('home'))

# 👉 Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)