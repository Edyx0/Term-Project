import storage
PRODUCT_FILE_PATH = "data/products.json"

def load_products(path: str) -> list:
    products = storage.load_json(path)
    print(products)
    return products


def save_products(products: list, path: str = PRODUCT_FILE_PATH) -> None:
    storage.write_json(path, products)
    print("Products saved")

def search_products(keyword: str, products: list,) -> list:
    results = []
    st = keyword.lower()

    for product in products:
        if (st in product["name"].lower() or st in product["description"].lower()):
            results.append(product)  
    return results


def filter_by_category(products: list, category: str) -> list:
    results = []
    match_category = category.lower()
    
    for product in products:
        if product["category"].lower() == match_category:
            results.append(product)
            
    return results


def update_product_stock(products: list, product_id: str, delta: int) -> bool:
    for product in products:
        if product.get("id") == product_id:
            product["stock"] += delta
            print(f"New Stock for product ID: {product_id} is {product['stock']}")
            return True


            
            

def add_new_product(products: list, product_data: dict) -> dict:
    products.append(product_data)
    return products

#test 
load_products("data/products.json")
#working 19.11.2025

    