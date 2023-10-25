

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': {'price': 50, 'special_offer': [{'count': 5, 'price': 200}, {'count': 3, 'price': 130}]},
        'B': {'price': 30, 'special_offer': [{'count': 2, 'price': 45}]},
        'C': {'price': 20, 'special_offer': []},
        'D': {'price': 15, 'special_offer': []},
        'E': {'price': 40, 'special_offer': []},
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
        else:
            return -1
    
    for item, count in item_count.items():
        special = price_table[item]['special_offer']
        unit_price = price_table[item]['price']

        if special:
            special_count = special['count']
            special_price = special['price']

            num_specials = count // special_count
            num_remaining = count % special_count

            total_price += (num_specials * special_price) + (num_remaining * unit_price)
        else: # no special
            total_price += count * unit_price
    
    return total_price

