from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

count = 0

@app.route('/')
def index():
    global count
    return render_template('index.html', count=count)

@app.route('/count-up')
def countup():
    global count
    count+=1
    return render_template('index.html', count=count)

@app.route('/count-down')
def countdown():
    global count
    count+=1
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
