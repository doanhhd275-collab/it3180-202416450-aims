import io
import unittest
from contextlib import redirect_stdout

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestMessages(unittest.TestCase):

    def test_full_cart_message(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            cart.add_dvd(DigitalVideoDisc(f"DVD {i}"))
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            cart.add_dvd(DigitalVideoDisc("DVD 21"))
        self.assertIn("The cart is full", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()