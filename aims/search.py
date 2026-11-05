def search_by_category(items, category):
    """Tim DVD theo the loai."""
    if not category or not category.strip():
        return []

    keyword = category.strip().casefold()

    return [
        dvd for dvd in items
        if keyword in dvd.category.casefold()
    ]



def search_by_title(items, title):
    """Tim DVD theo ten, khong phan biet hoa thuong."""
    if not title or not title.strip():
        return []

    keyword = title.strip().casefold()

    return [
        dvd for dvd in items
        if keyword in dvd.title.casefold()
    ]


