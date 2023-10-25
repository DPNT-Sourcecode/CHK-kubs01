

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': {'price': 50, 'special_offers': [{'count': 5, 'price': 200}, {'count': 3, 'price': 130}]},
        'B': {'price': 30, 'special_offers': [{'count': 2, 'price': 45}]},
        'C': {'price': 20, 'special_offers': []},
        'D': {'price': 15, 'special_offers': []},
        'E': {'price': 40, 'special_offers': []},
        'F': {'price': 10, 'special_offers': []},
        'G': {'price': 20, 'special_offers': []},
        'H': {'price': 10, 'special_offers': [{'count': 10, 'price': 80}, {'count': 5, 'price': 45}]},
        'I': {'price': 35, 'special_offers': []},
        'J': {'price': 60, 'special_offers': []},
        'K': {'price': 80, 'special_offers': [{'count': 2, 'price': 150}]},
        'L': {'price': 90, 'special_offers': []},
        'M': {'price': 15, 'special_offers': []},
        'N': {'price': 40, 'special_offers': []},
        'O': {'price': 10, 'special_offers': []},
        'P': {'price': 50, 'special_offers': [{'count': 5, 'price': 200}]},
        'Q': {'price': 30, 'special_offers': []},
        'R': {'price': 50, 'special_offers': []},
        'S': {'price': 30, 'special_offers': []},
        'T': {'price': 20, 'special_offers': []},
        'U': {'price': 40, 'special_offers': []},
        'V': {'price': 50, 'special_offers': []},
        'W': {'price': 20, 'special_offers': []},
        'X': {'price': 90, 'special_offers': []},
        'Y': {'price': 10, 'special_offers': []},
        'Z': {'price': 50, 'special_offers': []},
    }

    item_count = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
    }

    total_price = 0

    for item in skus:
        if item in item_count:
            item_count[item] += 1
        else:
            return -1
    
    if item_count['E'] >= 2:
        free_bs = item_count['E'] // 2
        item_count['B'] = max(0, item_count['B'] - free_bs)
    
    if item_count['F'] >= 3:
        free_fs = item_count['F'] // 3
        item_count['F'] -= free_fs
    
    for item, count in item_count.items():
        special_offers = sorted(price_table[item]['special_offers'], key=lambda x: x['count'], reverse=True)
        unit_price = price_table[item]['price']

        if special_offers:
            for special_offer in special_offers:
                special_count = special_offer['count']
                special_price = special_offer['price']

                num_specials = count // special_count
                count %= special_count

                total_price += num_specials * special_price
        
        total_price += count * unit_price
    
    return total_price






