import newrelic.agent
newrelic.agent.initialize('/Users/wtang/VSCodeProjects/pythonFlask/newrelic.ini', 'production')

import subprocess
label = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
result="SHA COMMIT " + label.decode('utf-8')
print(result)

from flask import Flask
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(500)

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/500')
def error500():
    abort(500)
