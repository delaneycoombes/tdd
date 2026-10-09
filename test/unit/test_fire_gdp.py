import os
import sys
import unittest
import fire_gdp 


DATA = os.path.join(os.path.dirname(__file__), '..', 'data')
CO2 = os.path.join(DATA, 'co2_small.csv')
GDP = os.path.join(DATA, 'gdp_small.csv')


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        self.assertEqual(fire_gdp.get_column_index(['a', 'b', 'c'], 'b'), 1)


class TestGetData(unittest.TestCase):

    def test_no_query(self):
        rows = fire_gdp.get_data(CO2)
        self.assertEqual(len(rows), 8)
        self.assertEqual(rows[0][0], 'Brazil')

    def test_query_match(self):
        rows = fire_gdp.get_data(CO2, 0, 'Brazil')
        self.assertEqual(len(rows), 5)
        for row in rows:
            self.assertEqual(row[0], 'Brazil')

    def test_return_header(self):
        header, rows = fire_gdp.get_data(CO2, return_header=True)
        self.assertEqual(header,
                         ['Area', 'Year', 'Forest fires', 'Other column'])
        self.assertEqual(len(rows), 8)
        

if __name__ == '__main__':
    unittest.main()
