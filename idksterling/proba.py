from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])  
def integer():
    message = ''  
    if request.method == 'POST':  
        user = request.form.get('username')
        password = request.form.get('password')
        message = message + user + ' ' + password  
        return render_template('proba.html', message=message)  
    return render_template('proba.html', message=message)

if __name__ == '__main__':
    print('run server')
    app.run()