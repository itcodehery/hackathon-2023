from database import db
 
# Declaring Model
class Client(db.Model):
    __tablename__ = "client"
 
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(150), nullable=False)
    c_type = db.Column(db.String(150), nullable=True)
    c_email = db.Column(db.String(150), nullable=False)
    c_pwd = db.Column(db.String(150), nullable=False)
    c_upi = db.Column(db.String(150), nullable=False)

class Vendor_Detail(db.Model):
    __tablename__ = "vendor_detail"

    v_id = db.Column(db.String(150), primary_key=True)
    v_name = db.Column(db.String(150), nullable=False)
    v_email = db.Column(db.String(150), nullable=False)
    v_pwd = db.Column(db.String(150), nullable=False)
    v_upi = db.Column(db.String(150), nullable=False)
    shop_no = db.Column(db.Integer, nullable=False)

class Vendor_Item(db.Model):
    __tablename__ = "vendor_item"

    item_id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.String(150), nullable=False, references='vendor_detail.v_id')
    item_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Real, nullable=False)
