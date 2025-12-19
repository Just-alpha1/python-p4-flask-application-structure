#!/usr/bin/env python3
"""
Flask Application Tutorial Demo
This file demonstrates the concepts from the Flask tutorial including:
- Flask app initialization
- Routing and views
- Request object manipulation
- Understanding __name__ variable
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    Tutorial Question Answer: 
    Which line of code tells Flask to show the returned data from index() in the web browser?
    
    Answer: The @app.route('/') decorator tells Flask to show the returned data from index() 
    in the web browser. This decorator registers the index() function as a view that handles 
    requests to the root URL (/).
    """
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    """
    Tutorial Question Answer:
    Flask has to parse "string" and "username" from the route. How can you use Python to 
    remove brackets and get parameters out of a string?
    
    Answer: Flask automatically parses the route parameters. The syntax '<string:username>' 
    tells Flask to expect a string parameter named 'username'. Flask's URL rule parser 
    handles the extraction - you don't need to manually remove brackets. The parameter 
    is passed directly to the function.
    """
    return f'<h1>Profile for {username}</h1>'

@app.route('/request-info')
def request_info():
    """
    Demonstrates request object manipulation and inspection
    """
    info = {
        'method': request.method,
        'path': request.path,
        'url': request.url,
        'base_url': request.base_url,
        'host': request.host,
        'remote_addr': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'content_type': request.content_type,
        'args': dict(request.args),
        'headers': dict(request.headers)
    }
    return jsonify(info)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """
    Demonstrates handling different HTTP methods and request data
    """
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        return f'<h1>Hello {name}! (POST request)</h1>'
    else:
        name = request.args.get('name', 'Guest')
        return f'<h1>Hello {name}! (GET request)</h1>'

@app.route('/debug-name')
def debug_name():
    """
    Tutorial Question Answer:
    What is the value of __name__ when we run python server/app.py?
    
    Answer: When running 'python server/app.py', __name__ equals '__main__'. 
    This is because the script is being executed directly, not imported as a module.
    """
    return f'<h1>Current __name__ value: {__name__}</h1>'

if __name__ == '__main__':
    """
    Tutorial Question Answer:
    Which line of code tells Flask to show the returned data from index() in the web browser?
    
    Answer: The app.run() method starts the Flask development server, which listens for 
    HTTP requests and routes them to the appropriate view functions. When you access the 
    application in a browser, the server handles the request and displays the response.
    """
    app.run(port=5555, debug=True)
