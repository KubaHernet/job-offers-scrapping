def remove_duplicates(items, selector):
    seen = set()
    unique_items = []
    for item in items:
        key = selector(item)
        if key and key not in seen:
            unique_items.append(item)
            seen.add(key)
    return unique_items