import pytest
import pandas as pd
from modules.section import UniversalColumn, SectionList


# Mock data for testing
mock_data = {
    "UC305x305x97": [
        "UC305x305x97",
        305,
        "97",
        97,
        305,
        305,
        10,
        20,
        15,
        270,
        10.0,
        15.3,
        345,
        1150,
        900,
        25.4,
        15.6,
        1290,
        750,
        17.1,
        10.9,
        86.2,
        52.6,
        1000,
        740,
        1.2,
        0.5,
        700,
        120,
        97,
    ]
}


# Mock the pandas read_json function to return the mock_data as a DataFrame
def mock_read_json(file_path, orient):
    return pd.DataFrame.from_dict(mock_data, orient="index")


pd.read_json = mock_read_json


def test_universal_column_creation():
    col = UniversalColumn.create("UC305x305x97")
    assert col.designation == "UC305x305x97"
    assert col.D == 305
    assert col.B == 305
    assert col.mass_per_metre == 97


def test_section_list():
    col1 = UniversalColumn.create("UC305x305x97")
    col2 = UniversalColumn.create("UC305x305x97")
    section_list = SectionList([col1, col2])

    assert len(section_list) == 2
    assert str(section_list) == "UC305x305x97, UC305x305x97"

    # Test iteration
    designations = [col.designation for col in section_list]
    assert designations == ["UC305x305x97", "UC305x305x97"]


if __name__ == "__main__":
    pytest.main()
    # coverage run -m pytest
    # coverage report -m
    # coverage html
