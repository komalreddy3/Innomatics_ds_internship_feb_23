
# Step 1 - To import FLASK
from flask import Flask, request

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return "Welcome to HOME PAGE"


@app.route('/upper')
def UpperCase():
    a = request.args.get('a')
    return a.upper()


###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)

