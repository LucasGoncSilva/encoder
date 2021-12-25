from flask import Flask, render_template, redirect, url_for, request

from functions import encode, decode


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/output', methods = ['POST', 'GET'])
def output():
    
    if request.method == 'POST' and request.form['encode_func'] == 'encode':
        
        message = request.form['message']
        keyword = request.form['keyword']

        output = str(encode(message, keyword))
        output = output[2:-1]

        return render_template('index.html', output=output)


    elif request.method == 'POST' and request.form['encode_func'] == 'decode':
        
        message = request.form['message']
        keyword = request.form['keyword']

        output = str(decode(message, keyword))
        output = output[2:-1]

        return render_template('index.html', output=output)


    else: return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug = True)