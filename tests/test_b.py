import unittest
from modules.section import UniversalColumn, SectionList


class TestUniversalColumn(unittest.TestCase):
    def setUp(self):
        self.uc = UniversalColumn.create(
            "UC1"
        )  # replace 'UC1' with a valid designation from your data

    def test_init(self):
        self.assertEqual(self.uc.designation, "UC1")

    def test_str(self):
        self.assertEqual(str(self.uc), "UC1")


class TestSectionList(unittest.TestCase):
    def setUp(self):
        self.sl = SectionList(
            [UniversalColumn.create("UC1"), UniversalColumn.create("UC2")]
        )  # replace 'UC1', 'UC2' with valid designations from your data

    def test_init(self):
        self.assertEqual(len(self.sl), 2)

    def test_str(self):
        self.assertEqual(str(self.sl), "UC1, UC2")


if __name__ == "__main__":
    unittest.main()
    # Test: coverage run -m unittest discover
    # & coverage report -m
