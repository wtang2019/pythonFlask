import newrelic.agent
newrelic.agent.initialize('/Users/wtang/VSCodeProjects/pythonFlask/newrelic.ini', 'production')

import subprocess
label = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
result="SHA COMMIT " + label.decode('utf-8')
print(result)

# Import the logging module and the New Relic log formatter
import logging
from newrelic.agent import NewRelicContextFormatter
logging.basicConfig(filename='record.log', level=logging.DEBUG)

# Instantiate a new log handler
handler = logging.StreamHandler()

# Instantiate the log formatter and add it to the log handler
formatter = NewRelicContextFormatter()
handler.setFormatter(formatter)

# Get the root logger and add the handler to it
root_logger = logging.getLogger()
root_logger.addHandler(handler)

from flask import Flask
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def hello():
    app.logger.info('Info level log')
    return 'Hello, World!'

@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        app.logger.warn('Error Level Message')
        abort(500)

@app.errorhandler(500)
def internal_error(error):
    app.logger.warn('Error Level 500')
    return render_template('500.html'), 500

@app.route('/500')
def error500():
    app.logger.warn('Error Level 500')
    abort(500)
