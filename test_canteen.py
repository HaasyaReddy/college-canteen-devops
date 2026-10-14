# Automated tests for College Canteen Food Ordering System

import unittest
import canteen


class CanteenTests(unittest.TestCase):

    def test_menu_display(self):
        menu = canteen.display_menu()
        self.assertIn("Sandwich", menu)

    def test_add_item_to_cart(self):
        cart = {}
        canteen.add_to_cart(cart, "Sandwich", 2)
        self.assertEqual(cart["Sandwich"], 2)

    def test_calculate_total(self):
        cart = {"Sandwich": 2, "Juice": 1}
        total = canteen.calculate_total(cart)
        self.assertEqual(total, 130)

    def test_invalid_food_item(self):
        with self.assertRaises(ValueError):
            canteen.add_to_cart({}, "Pizza", 1)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            canteen.add_to_cart({}, "Sandwich", 0)

    def test_place_order_with_empty_cart(self):
        with self.assertRaises(ValueError):
            canteen.place_order({})


if __name__ == "__main__":
    unittest.main()