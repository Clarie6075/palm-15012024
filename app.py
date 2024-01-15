from flask import Flask, request, render_template
import google.generativeai as palm
'''
Flask is the web framework used to create the application.
request is used to handle HTTP requests.
render_template is used to render HTML templates.
'''

'''
Configures the palm module with an API key.
Defines a model named "chat-bison-001." It is a generative AI model used for chat-based applications.
'''
palm.configure(api_key="AIzaSyDjUpw2XNjpSYnFyjLdB9uoT20S6YiprJY")
model = {"model":"models/chat-bison-001"}

# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])

def index():  # handling requests to the root URL ("/").

    if request.method =="POST":
        q = request.form.get("q")
        print(q)
        response = palm.chat(
        **model,messages = q
        )
        # it renders the "index.html" template and passes a variable result with the value "ML model not read".
        return(render_template("index.html",result = response.last))
    else:

        return(render_template("index.html",result = "waitting for question......"))

if __name__ =="__main__":
        app.run(host="127.0.0.1", port=8080)
