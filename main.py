import catalog
import cart
import orders
import storage

def sales_summary(all_orders):
    total_revenue = 0
    for order in all_orders:
        for item_id in order["items"]:
            item = order["items"][item_id]
            total_revenue += item["price"] * item["quantity"]
            
    return {
        "revenue": total_revenue,
        "order_count": len(all_orders)
    }

def admin_dashboard(products):
    try:
        all_orders = storage.load_json("data/orders.json")
    except:
        all_orders = []
        
    summary = sales_summary(all_orders)
    print("\n--- ADMIN DASHBOARD ---")
    print("Total Products in Catalog: " + str(len(products)))
    print("Total Orders Processed: " + str(summary["order_count"]))
    print("Total Revenue: $" + str(summary["revenue"]))

def customer_menu(products, active_cart):
    while True:
        print("\n--- CUSTOMER PORTAL ---")
        print("1. View Products")
        print("2. Search Products")
        print("3. Add to Cart")
        print("4. View Cart & Checkout")
        print("5. Back to Main Menu")
        
        choice = input("Choice: ")
        
        if choice == "1":
            for p in products:
                print(p["id"] + ": " + p["name"] + " - $" + str(p["price"]) + " (Stock: " + str(p["stock"]) + ")")
        elif choice == "2":
            term = input("Search term: ")
            results = catalog.search_products(term, products)
            for r in results:
                print(r["id"] + ": " + r["name"] + " - $" + str(r["price"]))
        elif choice == "3":
            pid = input("Product ID: ")
            qty = int(input("Quantity: "))
            found = False
            for p in products:
                if p["id"] == pid:
                    active_cart = cart.add_to_cart(active_cart, p, qty)
                    found = True
                    break
            if not found:
                print("Product not found.")
        elif choice == "4":
            if not active_cart:
                print("Cart is empty.")
                continue
            print("\nYOUR CART:")
            for item in active_cart.values():
                print(item["name"] + " x" + str(item["quantity"]))
            
            confirm = input("Checkout? (y/n): ")
            if confirm.lower() == "y":
                name = input("Enter your name: ")
                order = orders.create_order(active_cart, name, "Cash")
                
                try:
                    orders_list = storage.load_json("data/orders.json")
                except:
                    orders_list = []
                
                orders_list.append(order)
                storage.write_json("data/orders.json", orders_list)
                
                orders.update_inventory_after_order(products, order)
                catalog.save_products(products)
                orders.generate_receipt(order, "receipts")
                
                print("Order placed successfully!")
                active_cart.clear()
        elif choice == "5":
            break

def admin_menu(products):
    while True:
        print("\n--- ADMIN PORTAL ---")
        print("1. Admin Dashboard")
        print("2. Add New Product")
        print("3. Save Catalog")
        print("4. Back to Main Menu")
        
        choice = input("Choice: ")
        
        if choice == "1":
            admin_dashboard(products)
        elif choice == "2":
            pid = input("ID: ")
            name = input("Name: ")
            cat = input("Category: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            desc = input("Description: ")
            new_p = {"id": pid, "name": name, "category": cat, "price": price, "stock": stock, "description": desc}
            catalog.add_new_product(products, new_p)
        elif choice == "3":
            catalog.save_products(products)
        elif choice == "4":
            break

def main():
    storage.ensure_storage_structure(".")
    products = catalog.load_products("data/products.json")
    active_cart = {}

    while True:
        print("\n=== SHOPPING SYSTEM ===")
        print("1. Customer Portal")
        print("2. Admin Portal")
        print("3. Exit")
        
        mode = input("Select Mode: ")

        if mode == "1":
            customer_menu(products, active_cart)
        elif mode == "2":
            admin_menu(products)
        elif mode == "3":
            print("Closing system.")
            break

if __name__ == "__main__":
    main()