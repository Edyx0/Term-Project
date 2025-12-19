def Main():
    print("Shopping System Main Module")
    all_products = catalog.load_products()
    print(f"\nTotal products loaded: {len(all_products)}")