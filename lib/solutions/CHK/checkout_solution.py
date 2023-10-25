

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': {'price': 50, 'special_offer': {'count': 3, 'price': 130}},
        'B': {'price': 30, 'special_offer': {'count': 2, 'price': 45}},
        'C': {'price': 20, 'special_offer': None},
        'D': {'price': 15, 'special_offer': None},
    }

    item_count = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
    }

    total_price = 0

    for item in skus:
        if item in item_count:
            item_count[item] += 1

