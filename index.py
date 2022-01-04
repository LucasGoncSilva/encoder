from flask import Flask, render_template, redirect, url_for, request

from functions import encode, decode


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/output', methods = ['POST', 'GET'])
def banana():
    
    if request.method == 'POST' and request.form['encode_func'] == 'encode':
        
        output = encode(request.form['message'], request.form['keyword'])

        return render_template('index.html', output=output)


    elif request.method == 'POST' and request.form['encode_func'] == 'decode':
        
        output = decode(request.form['message'], request.form['keyword'])

        return render_template('index.html', output=output)


    else: return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug = True)