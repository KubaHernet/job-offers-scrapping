from typing import TypeVar, Callable, Optional

TListItem = TypeVar('TListItem')
TItemSelector = TypeVar('TItemSelector')

def remove_duplicates(
        items: list[TListItem],
        selector: Callable[[TListItem], Optional[TItemSelector]]
) -> list[TListItem]:
    seen: set[TItemSelector] = set()
    unique_items: list[TListItem] = []
    
    for item in items:
        key = selector(item)
        if key and key not in seen:
            unique_items.append(item)
            seen.add(key)

    return unique_items