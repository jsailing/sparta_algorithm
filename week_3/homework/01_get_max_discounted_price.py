shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort()

    max_discounted_price = 0
    for price in prices:
        if user_coupons:
            coupon = user_coupons.pop()
            max_discounted_price += price * (100 - coupon) // 100
        else:
            max_discounted_price += price

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.