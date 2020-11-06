from flask import Flask, render_template, request, url_for
import psycopg2

from werkzeug.utils import redirect

app = Flask(__name__)

con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="jcom",
    user="postgres",
    password="admin"
    )


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('./home.html')

@app.route('/login', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        Username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
        cur = con.cursor()
        cur.execute("insert into register (username,email,password) values (%s,%s,%s)", (Username, email, password))
        con.commit()
        cur.close()

        return redirect(url_for('register'))
    else:
        return render_template("register.html")


@app.route('/home2', methods=['GET'])
def home2():
    return render_template('home2.html')

@app.route("/status",methods=['GET'])
def status():
    import matplotlib.pyplot as plt

    cur = con.cursor()
    cur.execute("SELECT numberofmatch, numberofgoal, creaditsobtained FROM checktable ")
    values = cur.fetchall()
    print(values)
    con.commit()
    cur.close()

    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.bar(
        range(len(values)),
        [values[1] for values in values],
        tick_label=[values[0] for values in values]

    )
    plt.show()

    return render_template("status2.html")


#con.close( )
#Last line
if __name__ == '__main__':
    app.run(debug=True)



