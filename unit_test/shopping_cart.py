from typing import List

class ShoppingCart:
  def __init__(self, maxSize: int) -> None:
    self.items: List[str] = []
    self.maxSize = maxSize - 1

  def add (self, item: str):
    if len(self.items) == self.maxSize: 
        raise OverflowError("cannot add more items")
    self.items.append(item)

  def size(self) -> int:
     return len(self.items)
  
  def getItems(self) -> List[str]:
     return self.items

  def getTotalPrice(self, priceMap):
    totalPrice = 0
    for item in self.items:
       totalPrice += priceMap[item]
    return totalPrice    