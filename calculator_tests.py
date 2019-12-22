from calculator import calculate
import unittest

class Test(unittest.TestCase):
  def test1(self):
    self.assertEqual(calculate(['3', '*', '4']), 12)
  def test2(self):
    self.assertEqual(calculate(['5', '+', '6']), 11)
  def test4(self):
    self.assertEqual(calculate(['25', '*', '2']), 50)
  def test5(self):
    self.assertEqual(calculate(['15', '/', '15']), 1)
if __name__ == '__main__':
    unittest.main()
