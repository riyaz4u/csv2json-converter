import unittest
class test(unittest.TestCase):
    def test_openfile(self):
        self.assertTrue(True)

    def test_csvfile(self):
        result = "data.csv"
        self.assertEqual(result, "data.csv")

    def test_jsonfile(self):
        result = "data.json"
        self.assertEqual(result, "data.json")
if __name__=='__main__':
    unittest.main()