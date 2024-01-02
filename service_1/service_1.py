from flask import Flask

app = Flask(__name__)

@app.route('/do_something')
def do_something():
    # Define the functionality of service_1 when called
    # This is a placeholder, put your logic here
    return "Service 1 did something! because the condition was cat"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
