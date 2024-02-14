from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
  return ShoppingCart(5)

def testCanAddItemToCart(cart) :
  cart.add('apple')
  assert cart.size() == 1

def testWhenItemAddedThenCartContainsItem(cart):
  cart.add('apple')
  assert 'apple' in cart.getItems()

def testWhenAddedMoreThanMaxSizeItemsSholdFail(cart):
  for _ in range(4):
    cart.add("apple")
  with pytest.raises(OverflowError):
    cart.add("apple")

def testCanGetTotalPrice (cart):
  cart.add("apple")
  cart.add("orange")

  priceMap = { 
    "apple": 10,
    "orange": 20
  }
  assert cart.getTotalPrice(priceMap = priceMap) == 30

