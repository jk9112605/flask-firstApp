from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get(
            'username')  #can use get(<varialbe name>) to get value
        password = request.form[
            'password']  #or can use form[<varialbe name>] to get value

        if username == 'neuralnine' and password == 'password':
            return 'Success'
        else:
            return 'Failure'


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        return "this is excel file"

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']
    
    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
    
    return jsonify({'message': 'Successfully written!'})
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
