
from functions import *
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods=["POST","GET"])
def insert():
    if request.method == 'POST':
        ID = int(request.form.get("id"))
        name = str(request.form.get("name"))
        adress = str(request.form.get("adress"))
        phonenumber = str(request.form.get("phonenumber"))
        requisities = str(request.form.get("requisities"))
        worktime = request.form.get("Worktime")
        contact = request.form.get("contact")
        message = insert_into_client(ID, name, adress, phonenumber, requisities, contact, worktime)

    else:
        message=''
    return render_template("input.html", message=message)


@app.route('/clients')
def client():

    client_value = import_all_from_client()
    return render_template("client.html",  client_value=client_value)

@app.route('/store')
def store():

    store_value = import_all_from_store()
    return render_template("store.html",  store_value=store_value)

@app.route('/rent')
def rent():

    rent_value = import_all_from_rent()
    return render_template("rent.html",  rent_value=rent_value)


if __name__ == '__main__':
    app.run(debug=True)



