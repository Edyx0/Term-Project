from decimal import Decimal

def add_to_cart(cart, product, quantity):
    if quantity <= 0:
        print("Error: Quantity must be positive.") 
        return cart
    product_id = product.get("id")
    current_stock = product.get("stock", 0)

    requested_total = quantity
    if product_id in cart:
        requested_total += cart[product_id]["quantity"]
    if requested_total > current_stock:
        print("Error: Only " + str(current_stock) + " items in stock.")
        return cart
    if product_id in cart:
        cart[product_id]["quantity"] += quantity
    else:
        cart[product_id] = {
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }
    return cart

def remove_from_cart(cart, product_id):
    if product_id in cart:
        del cart[product_id]
    return cart

def update_quantity(cart, product_id, quantity):
    if quantity <= 0:
        return remove_from_cart(cart, product_id)
    if product_id in cart:
        cart[product_id]["quantity"] = quantity
    return cart
    
def calculate_totals(cart, tax_rate, discounts):
    subtotal = Decimal("0.00")
    for item in cart.values():
        subtotal += item["price"] * (int(item["quantity"]))

    total_discount = Decimal("0.00")
    for discount in discounts:
        total_discount += Decimal(str(discount))

    tax = (subtotal - total_discount) * Decimal(str(tax_rate))
    final_total = subtotal - total_discount + tax

    return {
        "subtotal": subtotal.quantize(Decimal("0.01")),
        "discount": total_discount.quantize(Decimal("0.01")),
        "tax": tax.quantize(Decimal("0.01")),
        "total": final_total.quantize(Decimal("0.01"))
    }

def apply_promo_code(cart, code, promo_rules):
    if code in promo_rules:
        return promo_rules[code]
    return {"type": "none", "value": 0}