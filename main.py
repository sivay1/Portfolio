import os
from flask import Flask,render_template,redirect,request,url_for,session

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('portfolio.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)))
