from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 餐點資料
menu_items = [
    {"id": 1, "name": "薯條", "price": 50, "size": "中"},
    {"id": 2, "name": "漢堡", "price": 100, "size": "中"},
    {"id": 3, "name": "可樂", "price": 30, "size": "中"}
]

# 已確認餐點
current_orders = []

@app.route("/")
def index():
    return render_template("index.html", menu_items=menu_items)

@app.route("/item/<int:item_id>")
def item(item_id):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if not item:
        return "餐點不存在", 404
    return render_template("item.html", item=item)

@app.route("/edit/<int:item_id>", methods=["POST"])
def edit_item(item_id):
    size = request.form.get("size", "中")
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if item:
        current_orders.append({"name": item["name"], "price": item["price"], "size": size})
    return redirect(url_for("index"))

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    return redirect(url_for("index"))

@app.route("/current")
def current():
    total_price = sum(order["price"] for order in current_orders)
    return render_template("current.html", orders=current_orders, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True)
