from flask import Flask,url_for,render_template
from auth import auth
import random
import pandas as pd

app = Flask(__name__)
app.register_blueprint(auth.bp)

@app.route('/')
def index():
    name = 'spread11'
    dataFrame = get_dataFrame()
    return render_template('index.html',name=name,dataFrame=dataFrame)


def get_dataFrame()->pd.DataFrame:
    data = [['xxx',67,92,85],['yyy',78,97,65],['zzz',92,79,85]]

    return pd.DataFrame(data,columns=['姓名','國文','數學','英文'])