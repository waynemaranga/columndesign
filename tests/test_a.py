import unittest
from modules.section import UniversalColumn, SectionList
import os
import json
import pandas as pd


class TestUniversalColumn(unittest.TestCase):

    def setUp(self):
        self.uc_json = os.path.join(os.getcwd() + "/db/uc_bs5950.json")
        self.uc_df = pd.read_json(self.uc_json, orient="index")

    def test_init(self):
        designation = self.uc_df.index[0]
        column = UniversalColumn(designation)
        self.assertEqual(column.designation, designation)

    def test_str(self):
        designation = self.uc_df.index[0]
        column = UniversalColumn(designation)
        self.assertEqual(str(column), designation)

    def test_create(self):
        designation = self.uc_df.index[0]
        column = UniversalColumn.create(designation)
        self.assertEqual(column.designation, designation)


class TestSectionList(unittest.TestCase):

    def setUp(self):
        self.sections = [UniversalColumn(i) for i in self.uc_df.index[:2]]

    def test_init(self):
        section_list = SectionList(self.sections)
        self.assertEqual(section_list.sections, self.sections)

    def test_iter(self):
        section_list = SectionList(self.sections)
        self.assertEqual(list(section_list), self.sections)

    def test_len(self):
        section_list = SectionList(self.sections)
        self.assertEqual(len(section_list), len(self.sections))

    def test_str(self):
        section_list = SectionList(self.sections)
        self.assertEqual(
            str(section_list), ", ".join([i.designation for i in self.sections])
        )


if __name__ == "__main__":
    unittest.main()
    # Test: coverage run -m unittest discover && coverage report -m
