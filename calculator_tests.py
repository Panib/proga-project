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
  def test_unary_log10(self):
    self.assertAlmostEqual(calculate(['80', 'log10']), 1.9030899869919435856412166841735)
  def test_cos(self):
    self.assertAlmostEqual(calculate(['3.14', 'cos']), -0.999998731727539545285)
if __name__ == '__main__':
    unittest.main()
