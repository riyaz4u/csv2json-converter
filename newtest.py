import unittest
import os
class test(unittest.TestCase):

    def test_open_csv(self):
        DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(DIR, 'data.csv')
        self.assertTrue(os.path.exists(file_path))

    def test_select_csv(self):
        select_file = 'data.csv'
        select_file_path = 'C:/Users/Hello/Desktop/csv2jsonconverter/data.csv'

    def select(select_file, select_file_path):
            self.assertTrue(select(select_file, select_file_path))

    def test_convert_csv2json(self):
        result = 'data.json'
        self.assertEqual(result, 'data.json')

    def test_jsonfile(self):
        filename = 'data.json'
        path = 'C:/Users/Hello/Desktop/csv2jsonconverter/data.json'

    def jsonfile(filename, path):
            self.assertEqual(jsonfile(filename, path), 'data.json')


if __name__ == '__main__':
    unittest.main()