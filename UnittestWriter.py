import unittest
import Writer

class TestWriter(unittest.TestCase):
    def test_nameOfFile(self):
        self.assertAlmostEqual(Writer.ReadFromFile('sdasdas'),-1)

if __name__ == "__main__":
    unittest.main()