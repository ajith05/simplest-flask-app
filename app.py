from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def homepage():
    time_now = time.strftime("%d-%m-%Y %I:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {}.</p>
    
    <p>Refresh the page to update the time</p>
    """.format(time_now)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
