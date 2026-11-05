from aims.dvd import DigitalVideoDisc
from aims.cart import Cart
from aims.search import search_by_title, search_by_category

def main():
    print("AIMS-mini v1.0.0\n")
    cart = Cart()
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=18.99))
    cart.print_cart()
        # Test search by title
    print("\nSearch results for 'Star':")

    results = search_by_title(cart.items, "Star")
    

    if results:
        for dvd in results:
            print(dvd)
    else:
        print("No DVD found")
    print("\nSearch results for 'Harry Potter':")

    results = search_by_title(cart.items, "Harry Potter")

    if not results:
        print("No DVD found")
    print(f"Total cost: {cart.total_cost():.2f} $")
    print("\nSearch results for category 'Animation':")
    results = search_by_category(cart.items, "Animation")

    for dvd in results:
        print(dvd)


if __name__ == "__main__":
    main()
