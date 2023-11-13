from flask import Flask, render_template
from database import db


app = Flask(__name__)

#database configuration
db_name = 'eatcaias.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#database creation
def create_db():
    with app.app_context():
        db.create_all()
 
if __name__ == "__main__":
    from models import Client, Vendor_Detail, Vendor_Item
    create_db()

quantity = 1

#routes
@app.route("/")
def index():
    return render_template('main.html')

@app.route("/stuteachlogin")
def stuteachlogin():
    return render_template('st-login.html')

@app.route("/studteach")
def studteach():
    return render_template('studteach.html')

@app.route("/vendor")
def vendor():
    return render_template('vendor.html')

@app.route("/vendor-menu")
def vendor_menu():
    return render_template('vendor-menu.html', quantity=quantity)

@app.route('/increment')
def increment():
    global quantity
    quantity += 1
    return f'Counter has been incremented. <a href="/vendor-menu">Back</a>'

@app.route('/decrement')
def decrement():
    global quantity
    if quantity > 1:
        quantity -= 1
    return f'Counter has been decremented. <a href="/vendor-menu">Back</a>'