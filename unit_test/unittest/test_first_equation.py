import unittest
from first_equation import find_x

class TestFirst (unittest.TestCase):
  def test_find_x(self):
    args = (10, 10)
    self.assertEqual(find_x(*args), -1)
    args = (0, 0)
    self.assertEqual(find_x(*args), "ALL")
    args = (0, 10)
    self.assertEqual(find_x(*args), "NONE")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    