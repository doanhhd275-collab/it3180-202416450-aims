MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return

        for item in self.items:
            print(item)

    def search_by_title(self, title):
        """Tìm DVD theo tên, không phân biệt chữ hoa/chữ thường."""
        if not title or not title.strip():
            return []

        keyword = title.strip().casefold()

        return [
            dvd for dvd in self.items
            if keyword in dvd.title.casefold()  
        ]###