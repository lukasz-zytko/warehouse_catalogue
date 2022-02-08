from flask import Flask, redirect, render_template, request, url_for
import models
import forms
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "warehouse2022"
"""
product01 = models.Product(name="Barcelo", unit="litr", unit_price = 125, quantity = 10)
product02 = models.Product(name="Cygara", unit="sztuki", unit_price = 65, quantity = 50)
product03 = models.Product(name="Czekoladki", unit="sztuki", unit_price = 27, quantity = 100)
product04 = models.Product(name="Wino", unit="litr", unit_price = 125, quantity = 25)

ITEMS = {"Barcelo": product01, "Cygara": product02, "Czekoladki": product03, "Wino": product04}
"""
ITEMS = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products", methods = ["GET", "POST"])
def product_list():
    product_list = ITEMS
    item = "nic"
    form = forms.ProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            item = models.product_create(form.data)
            name = form.data["name"]
            ITEMS[name] = item

    return render_template("product-list.html", products=product_list, form=form, dane=item, klasa=ITEMS)

@app.route("/sell/<product_name>", methods=["GET", "POST"])
def sell_product(product_name):
    data = ITEMS[product_name]
    form = forms.Sell()
    quantity = "none"
    if request.method == "POST":
        ITEMS[product_name].quantity -= form.data["quantity"]
        return redirect(url_for("product_list"))
    return render_template("product.html", data=data, form=form, quantity=quantity)

@app.route("/export")
def export():
    with open("warehouse.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "unit", "unit_price", "quantity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in ITEMS.items():
            writer.writerow({"name": key, "unit": value.unit, "unit_price": value.unit_price, "quantity": value.quantity})
    return (redirect(url_for("product_list")))

@app.route("/import")
def import_data():
    with open("warehouse.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ITEMS[row["name"]] = models.Product(name=row["name"], unit=row["unit"], unit_price=float(row["unit_price"]), quantity=int(row["quantity"]))
    return (redirect(url_for("product_list")))

if __name__ == "__main__":
    app.run(debug=True)

#{{ url_for('list_products') }}