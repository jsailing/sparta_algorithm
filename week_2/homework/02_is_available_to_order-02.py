shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# O(N) * O(N) = O(N^2)
def is_available_to_order(menus, orders):
    for order in orders: # O(N)
        if order not in menus: # O(N)
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
