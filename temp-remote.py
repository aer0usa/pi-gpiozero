from flask import Flask
from flask import render_template
from thermostat import thermostat_setting, immediate_fahrenheit

app = Flask(__name__)
#app.debug = True # Uncomment to debug

@app.route('/')
def home():
    return render_template('hello.html',name='Temperature')

@app.route('/getTemp')
def getTemp():
    # return true;
    return render_template('response.html',name='Temperature',temperature=immediate_fahrenheit(),thermostat=thermostat_setting())

if __name__ == '__main__':
    app.run(host='0.0.0.0')

