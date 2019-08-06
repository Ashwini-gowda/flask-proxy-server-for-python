from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mypgm_db'

mysql = MySQL(app)

@app.route('/form-example', methods=['GET','POST'])
def form_example():
    if request.method == 'POST': 
	id = request.form['id']
        language = request.form['language']
        framework = request.form['framework']
	cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mypgm(id, language, framework) VALUES (%s, %s, %s)", (id, language, framework))
        mysql.connection.commit()
	
	cur.execute("SELECT * FROM mypgm")
	rows = cur.fetchall()
	resp = jsonify(rows)
	resp.status_code = 200
	cur.close()
	return resp
        
       

    return '''<form method="POST">
		  Id: <input type="text" name="id"><br>
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>''' 

@app.route('/form-process', methods=['GET','POST'])
def form_process():
    if request.method == 'POST':
	id = request.form['id'] 
        username = request.form['username']
        emailid = request.form['emailid']
	password = request.form['password']


        return jsonify(id=id, username=username, emailid=emailid, password=password)

    return '''<form method="POST">
		  Id: <input type="text" name="id"><br>
                  UserName: <input type="text" name="username"><br>
                  Emailid: <input type="text" name="emailid"><br>
		  password: <input type="password" name="password"><br>
                  <input type="submit" value="Submit"><br>
              </form>''' 
 
if __name__ == "__main__":
    app.run(debug='true')
