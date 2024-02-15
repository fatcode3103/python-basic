import unittest
import list_value

class TestStringMethod(unittest.TestCase):
  def test_create_tuple(self):
    data = "Python is a best language"
    result_list = list_value.create_value(data)

    self.assertIsInstance(result_list, list, "The returned data is not in the correct list format")
    for item in result_list:
      self.assertIsInstance(item, tuple, "The returned data is not in the correct tuple format")

if __name__ == '__main__':
  unittest.main(verbosity=2)