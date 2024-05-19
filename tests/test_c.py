import unittest
from unittest.mock import patch
import pandas as pd
from modules.section import UniversalColumn, SectionList


class TestUniversalColumn(unittest.TestCase):
    @patch("pandas.read_json")
    def test_universal_column(self, mock_read_json):
        mock_data = pd.DataFrame(
            {
                "designation": ["UC203x203x60"],
                "serial_size": [60],
                "additional": [None],
                "mass_per_metre": [60.4],
                "D": [203.0],
                "B": [203.0],
                "t": [8.6],
                "T": [12.7],
                "r": [10.2],
                "d": [164.4],
                "d_t": [172.8],
                "b_T": [177.6],
                "C": [1.0],
                "N": [1.0],
                "n": [1.0],
                "SA_m": [0.0],
                "SA_t": [0.0],
                "I_xx": [8.92e6],
                "I_yy": [1.59e6],
                "r_xx": [79.1],
                "r_yy": [33.3],
                "Z_xx": [88.1e3],
                "Z_yy": [15.7e3],
                "S_xx": [865.0],
                "S_yy": [154.0],
                "u": [0.836],
                "x": [0.601],
                "H": [0.599],
                "J": [0.282],
                "A": [76.8],
            }
        )
        mock_read_json.return_value = mock_data

        uc = UniversalColumn.create("UC203x203x60")
        self.assertEqual(str(uc), "UC203x203x60")
        self.assertEqual(uc.designation, "UC203x203x60")
        self.assertEqual(uc.serial_size, 60)
        self.assertEqual(uc.additional, None)
        self.assertEqual(uc.mass_per_metre, 60.4)
        self.assertEqual(uc.D, 203.0)
        self.assertEqual(uc.B, 203.0)
        self.assertEqual(uc.t, 8.6)
        self.assertEqual(uc.T, 12.7)
        self.assertEqual(uc.r, 10.2)
        self.assertEqual(uc.d, 164.4)
        self.assertEqual(uc.d_t, 172.8)
        self.assertEqual(uc.b_T, 177.6)
        self.assertEqual(uc.C, 1.0)
        self.assertEqual(uc.N, 1.0)
        self.assertEqual(uc.n, 1.0)
        self.assertEqual(uc.SA_m, 0.0)
        self.assertEqual(uc.SA_t, 0.0)
        self.assertEqual(uc.I_xx, 8.92e6)
        self.assertEqual(uc.I_yy, 1.59e6)
        self.assertEqual(uc.r_xx, 79.1)
        self.assertEqual(uc.r_yy, 33.3)
        self.assertEqual(uc.Z_xx, 88.1e3)
        self.assertEqual(uc.Z_yy, 15.7e3)
        self.assertEqual(uc.S_xx, 865.0)
        self.assertEqual(uc.S_yy, 154.0)
        self.assertEqual(uc.u, 0.836)
        self.assertEqual(uc.x, 0.601)
        self.assertEqual(uc.H, 0.599)
        self.assertEqual(uc.J, 0.282)
        self.assertEqual(uc.A, 76.8)


class TestSectionList(unittest.TestCase):
    def test_section_list(self):
        uc1 = UniversalColumn("UC203x203x60")
        uc2 = UniversalColumn("UC203x203x46")
        section_list = SectionList([uc1, uc2])

        self.assertEqual(len(section_list), 2)
        self.assertEqual(str(section_list), "UC203x203x60, UC203x203x46")

        for section in section_list:
            self.assertIsInstance(section, UniversalColumn)


if __name__ == "__main__":
    unittest.main()
    # // python3 test_universal_column.py
    # coverage run -m unittest discover -s tests -p "test_*.py"
    # coverage report -m
    # coverage html
