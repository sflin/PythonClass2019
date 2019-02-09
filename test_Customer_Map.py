import unittest
import Customer_Map_E3 as CM


class TestSuite(unittest.TestCase):

    def test_table_not_empty(self):
        self.assertGreaterEqual(
            len(CM.demographics.index),
            0,
            "demographics table seems to be empty, make sure that the csv file is available and read in properly"
        )
