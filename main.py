import catalog
import cart
import orders
import storage

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
            print("Customer mode active.")         
        elif mode == "2":
            admin_menu(products)
        elif mode == "3":
            print("Closing system.")
            break
if __name__ == "__main__":
    main()

def sales_summary(orders):
    # Calculates total revenue and order count [cite: 61]
    total_revenue = 0
    for order in orders:
        # Simplest way to sum totals if you haven't stored them yet
        for item_id in order["items"]:
            item = order["items"][item_id]
            total_revenue += item["price"] * item["quantity"]
            
    return {
        "revenue": total_revenue,
        "order_count": len(orders)
    }

def admin_dashboard(products, orders):
    summary = sales_summary(orders)
    print("ADMIN DASHBOARD")
    print("Total Products in Catalog: " + str(len(products)))
    print("Total Orders Processed: " + str(summary["order_count"]))
    print("Total Revenue: $" + str(summary["revenue"]))