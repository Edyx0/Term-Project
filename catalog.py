import storage

PRODUCT_FILE_PATH = "data/products.json"

def load_products(path):
    products = storage.load_json(path)
    return products

def save_products(products, path = PRODUCT_FILE_PATH):
    storage.write_json(path, products)
    print("Products saved")

def search_products(keyword, products):
    results = []
    st = keyword.lower()

    for product in products:
        if (st in product["name"].lower() or st in product["description"].lower()):
            results.append(product)  
    return results

def filter_by_category(products, category):
    results = []
    match_category = category.lower()
    
    for product in products:
        if product["category"].lower() == match_category:
            results.append(product)
            
    return results

def update_product_stock(products, product_id, delta):
    for product in products:
        if product.get("id") == product_id:
            if product["stock"] + delta < 0:
                return False
            product["stock"] += delta
            return True
    return False

def add_new_product(products, product_data):
    products.append(product_data)
    return products