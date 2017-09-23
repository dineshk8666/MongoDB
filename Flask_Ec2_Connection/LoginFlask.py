from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL
#from flask.ext.mysql import MySQL
# from werkzeug import generate_password_hash, check_password_hash
#import win32api  # An included library with Python install.

# _hashed_password = generate_password_hash(_password)
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ssspl2017'
app.config['MYSQL_DATABASE_DB'] = 'bucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('login.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showLogin')
def showLogin():
    return render_template('login.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        # json.dumps({'html': '<span>All fields good !!</span>'})
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser', (_name, _email, _password))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            # win32api.MessageBox(0, 'hello', 'User created successfully !')
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

            # return json.dumps({'html': '<span>All fields good !!</span>'})

    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/login', methods=['POST'])
def Login():
    # read the posted values from the UI
    _name = request.form['id_username']
    _password = request.form['id_password']
    loginid = 0

    # validate the received value
    if _name and _password:
        # json.dumps({'html': '<span>All fields good !!</span>'})
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_authenticate', (_name, _password, loginid))
        cursor.execute('Select @_sp_authenticate_2')
        data = cursor.fetchone()

        if int(data[0]) > 0:
            conn.commit()

            # return json.dumps({'html': '<span>All fields good !!</span>'})
            return json.dumps({'message': 'successfully Logged in  !'})

        else:

            return json.dumps({'error': str(data[0])})


    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run()
