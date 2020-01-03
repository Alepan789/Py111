import unittest
import math
from Tasks.b2_Taylor import ex, sinx


class MyTestCase(unittest.TestCase):
	def test_ex(self):
		const = 1.55433
		self.assertAlmostEqual(math.exp(const), ex(const), delta=0.0001, msg="More accurate! :D")

	def test2_ex(self):
		const = 1.55433
		self.assertAlmostEqual(math.exp(const), ex(const, 0.0001), delta=0.000001, msg="More accurate part2! :D")

	def test_sinx(self):
		const = 1.55433
		self.assertAlmostEqual(math.sin(const), sinx(const), delta=0.0001, msg="More accurate! :D")

	def test2_sinx(self):
		const = 1.55433
		self.assertAlmostEqual(math.sin(const), sinx(const, 0.0001), delta=0.00000001, msg="More accurate! :D")


if __name__ == '__main__':
	unittest.main()
