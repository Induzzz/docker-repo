from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
  return '<h1><center>Flask Application Version</center></h1>'

# Run the application if the script is executed directly
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080,debug=True)
