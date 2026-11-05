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

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
    def test_count(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A"))
        cart.add_dvd(DigitalVideoDisc("B"))
        self.assertEqual(cart.count(), 2)
    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("b"))
        cart.add_dvd(DigitalVideoDisc("A"))
        titles = [dvd.title for dvd in cart.sort_by_title()]
        self.assertEqual(titles, ["A", "b"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("B", cost=10.0))
        costs = [dvd.cost for dvd in cart.sort_by_cost()]
        self.assertEqual(costs, [10.0, 20.0])


if __name__ == "__main__":
    unittest.main()