import unittest
from coverage import Coverage
from modules.section import UniversalColumn, SectionList


class TestUniversalColumn(unittest.TestCase):

    def setUp(self):
        self.valid_designation = "152x152x23"
        self.invalid_designation = "INVALID"
        self.col = UniversalColumn.create(self.valid_designation)

    def test_create_valid_designation(self):
        self.assertIsInstance(self.col, UniversalColumn)
        self.assertEqual(self.col.designation, self.valid_designation)

    def test_create_invalid_designation(self):
        with self.assertRaises(KeyError):
            UniversalColumn.create(self.invalid_designation)

    def test_str(self):
        self.assertEqual(str(self.col), self.valid_designation)


class TestSectionList(unittest.TestCase):

    def setUp(self):
        self.sections = [
            UniversalColumn.create("102x102x12"),
            UniversalColumn.create("127x127x16"),
            UniversalColumn.create("152x152x23"),
        ]
        self.sec_list = SectionList(self.sections)

    def test_init(self):
        self.assertEqual(len(self.sec_list), 3)

    def test_iter(self):
        desigs = [str(col) for col in self.sec_list]
        expected_desigs = ["102x102x12", "127x127x16", "152x152x23"]
        self.assertEqual(desigs, expected_desigs)

    def test_len(self):
        self.assertEqual(len(self.sec_list), 3)

    def test_str(self):
        self.assertEqual(str(self.sec_list), "102x102x12, 127x127x16, 152x152x23")


if __name__ == "__main__":
    cov = Coverage()
    cov.start()

    # Run the tests
    suite = unittest.TestLoader().loadTestsFromModule(TestUniversalColumn)
    unittest.TextTestRunner().run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(TestSectionList)
    unittest.TextTestRunner().run(suite)

    # Generate coverage report
    cov.stop()
    cov.save()
    cov.report()
    # cov.html_report()
