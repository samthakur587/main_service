from flask import Flask
import requests

app = Flask(__name__)

@app.route('/check_condition/{check}}')
def check_condition(check:str):
    if check == 'yes':
        try:
            response = requests.get('http://10.142.0.7:8079/')
            print(response)
        except requests.exceptions.ConnectionError:
            print("Service 1 is unavailable")
            return "Service 1 unavailable"
    else:  
        try:
            response = requests.get('http://service2:5002/do_something')
            print(response)
        except requests.exceptions.ConnectionError:
            print("Service 3 is unavailable")
            return "Service 3 unavailable"
    return response.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
