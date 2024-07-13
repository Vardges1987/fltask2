from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return redirect(url_for('welcome'))
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect(url_for('welcome')))
    response.set_cookie('username', name, max_age=60 * 60 * 24)
    response.set_cookie('useremail', email, max_age=60 * 60 * 24)
    return response


@app.route('/welcome')
def welcome():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('welcome.html', username=username)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    response.delete_cookie('useremail')
    return response


if __name__ == '__main__':
    app.run(debug=True)
