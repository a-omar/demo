from unittest import TestCase
from unittest.mock import MagicMock, patch
from demo.continuous_delivery import ShoppingCart, Database

cart = ShoppingCart()

class TestShoppingCart(TestCase):

    def test_get_products_db(self):
        #Face database connection and result
        cur = MagicMock()
        cur.return_value = 3
        cart.Products = cur.return_value
        self.assertEquals(cart.get_products(),3)

    def test_remove_products(self):
        self.assertEquals(cart.get_products(),3)
        cart.remove_products(2)
        self.assertEquals(cart.get_products(),1)
        self.assertNotEqual(cart.get_products(),2)

    def test_reset(self):
        cart.Products = 0


class IntegrationTestShoppingCart(TestCase):

    def test_get_products_db(self):
        #Face database connection and result
        db = Database()
        cart.Products = db.query("select count(*) from cart")
        self.assertEquals(cart.get_products(),3)

    def test_remove_products(self):
        cart.remove_products(2)
        self.assertEquals(cart.get_products(),1)


    def test_reset(self):
        cart.Products = 0

if __name__ == '__main__':
    IntegrationTestShoppingCart().test_get_products_db()
    IntegrationTestShoppingCart().test_remove_products()
    IntegrationTestShoppingCart().test_reset()

    # TestShoppingCart().test_get_products_db()
    # TestShoppingCart().test_remove_products()
    # TestShoppingCart().test_reset()