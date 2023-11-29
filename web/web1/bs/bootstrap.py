import pandas as pd
from flask import Blueprint,render_template
from . import datasource
bp = Blueprint('bs', __name__, url_prefix='/bs')
@bp.route("/")
def index():
    return render_template("bs/index.html")

@bp.route("/test1")
def test():
    data:list[tuple]=datasource.lastest_datetime_data()
    dataFrame=pd.DataFrame(data)
    print(dataFrame)
    return render_template("bs/test1.html",data=data)

@bp.route("/product")
def product():
    return render_template("bs/product.html")
@bp.route("/profile")
def profile():
    return render_template("bs/profile.html")