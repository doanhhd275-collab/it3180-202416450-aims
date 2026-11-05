import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        dvd = DigitalVideoDisc("DVD 21")
        self.assertFalse(cart.add_dvd(dvd))
    def total_cost_with_discount(self, percent):
        """Tổng tiền sau khi giảm percent%."""
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

if __name__ == "__main__":
    unittest.main()