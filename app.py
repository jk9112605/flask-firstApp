from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    myvalue= 'NeuralNine'
    myresult = 10 + 20
    return render_template('index.html', myvalue=myvalue, myresult=myresult)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
