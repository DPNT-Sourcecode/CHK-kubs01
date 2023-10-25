

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
        'K': {'price': 70, 'special_offers': [{'count': 2, 'price': 150}]},
        'L': {'price': 90, 'special_offers': []},
        'M': {'price': 15, 'special_offers': []},
        'N': {'price': 40, 'special_offers': []},
        'O': {'price': 10, 'special_offers': []},
        'P': {'price': 50, 'special_offers': [{'count': 5, 'price': 200}]},
        'Q': {'price': 30, 'special_offers': [{'count': 3, 'price': 80}]},
        'R': {'price': 50, 'special_offers': []},
        'S': {'price': 20, 'special_offers': []},
        'T': {'price': 20, 'special_offers': []},
        'U': {'price': 40, 'special_offers': []},
        'V': {'price': 50, 'special_offers': [{'count': 3, 'price': 130}, {'count': 2, 'price': 90}]},
        'W': {'price': 20, 'special_offers': []},
        'X': {'price': 17, 'special_offers': []},
        'Y': {'price': 20, 'special_offers': []},
        'Z': {'price': 21, 'special_offers': []},
    }

    item_count = {item: 0 for item in price_table.keys()}

    total_price = 0

    for item in skus:
        if item in item_count:
            item_count[item] += 1
        else:
            return -1
    
    special_cases = {
        'E': ('B', 2),
        'F': ('F', 3),
        'N': ('M', 3),
        'R': ('Q', 3),
        'U': ('U', 4),
    }
    for item, (free_item, required_count) in special_cases.items():
        free_count = item_count[item] // required_count
        item_count[free_item] = max(0, item_count[free_item] - free_count)
    
    group_items = ['S', 'T', 'X', 'Y', 'Z']
    group_count = sum(item_count[item] for item in group_items)
    group_special_count = group_count // 3
    total_price += group_special_count * 45

    for _ in range(group_special_count * 3):
        max_item = max(group_items, key=lambda x: price_table[x]['price'])
        if item_count[max_item] > 0:
            item_count[max_item] -= 1

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
