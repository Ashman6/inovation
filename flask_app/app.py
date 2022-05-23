from flask import Flask, render_template, redirect
from views import my_view

app = Flask(__name__)

app.register_blueprint(my_view)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)

# @app.route("/")    
# def home():

#     return render_template('index.html')

# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

