import storage
import catalog
import time

def create_order(cart, customer, payment_method):
    order_id = str(int(time.time()))
    
    order = {
        "order_id": order_id,
        "customer": customer,
        "items": cart,
        "payment_method": payment_method
    }
    return order

def save_order(path, order):
    all_orders = storage.load_json(path)
    all_orders.append(order)
    storage.write_json(path, all_orders)

def update_inventory_after_order(products, order):
    for item_id in order["items"]:
        qty = order["items"][item_id]["quantity"]
        catalog.update_product_stock(products, item_id, -qty)
    return products

def generate_receipt(order, directory):
    filename = directory + "/receipt_" + order["order_id"] + ".txt"
    file = open(filename, "w")
    file.write("RECEIPT\n")
    file.write("Order ID: " + order["order_id"] + "\n")
    file.write("Customer: " + order["customer"] + "\n")
    file.write("-" * 20 + "\n")
    
    for item_id in order["items"]:
        item = order["items"][item_id]
        file.write(item["name"] + " x" + str(item["quantity"]) + "\n")
        
    file.close()
    return filename