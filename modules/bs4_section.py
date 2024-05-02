# A Section Object

import os
import pandas as pd
from collections import OrderedDict
from pandas import DataFrame

# To create UB object, the fn. is done inside the class.
# Data needs to be read from the db, in json/toml
# ... but reading from JSON everytime an object is created is costly i.e it's file i/o
# Fix: read json obj. once, create Pandas DataFrame, read from DataFrame
# TODO: create several Dataframes for UB, UC, angles etc once.

cwd = os.getcwd()
# print(cwd)
# print(os.listdir(cwd))
ub_json = os.path.join(cwd + "/data/ub_bs4.json")
# uc_json = os.path.join(cwd + "/db/uc.json")
# print(ub_json)
ub_df = pd.read_json(ub_json, orient="index")
# ... orient arg. encodes/decods the dataframe using index formatted JSON (as opposed to split,records etc)
# print(ub_df)
# for i in ub_df.columns:
#     print(i)


class UniversalSection:
    # for use with UB and UC, other section types to be made later
    # BS5950/BS4 sections, EN 10365 to be made based on this
    def __init__(self, df, designation):
        #! FIXME: refactor implementations for addition of default argument, or, create UB and UC to take relevant default df args
        data = df.loc[designation]

        (
            self.designation,
            self.serial_size,
            self.additional,
            self.mass_per_metre,
            self.D,
            self.B,
            self.t,
            self.T,
            self.r,
            self.d,
            self.d_t,
            self.b_T,
            self.C,
            self.N,
            self.n,
            self.SA_m,
            self.SA_t,
            self.I_xx,
            self.I_yy,
            self.r_xx,
            self.r_yy,
            self.Z_xx,
            self.Z_yy,
            self.S_xx,
            self.S_yy,
            self.u,
            self.x,
            self.H,
            self.J,
            self.A,
        ) = data

    def essentials(self):
        """Essential section data for FCE432"""
        essentials = [
            self.D,
            self.B,
            self.mass_per_metre,
            self.t,
            self.T,
            self.r,
            self.d,
            self.d_t,
            self.b_T,
            self.I_xx,
            self.r_yy,
            self.Z_xx,
            self.S_xx,
            self.u,
            self.x,
            self.designation,  # FIXME: #*HOTFIX: move to first
        ]

        return essentials

    def __str__(self) -> str:
        return f"{self.designation}"

    @staticmethod
    def create(df, designation):
        """Create section by section designation"""
        return UniversalSection(df, designation)

    @staticmethod
    def create_serial_size(df, serial_size):
        """Create list of sections by serial size"""
        sections = []
        for designation, data in df.iterrows():
            if data["SerialSize"] == serial_size:
                sections.append(UniversalSection(df, designation))  # list of objects

        sections_list = [section.designation for section in sections]
        return sections_list

    def get_essentials(self):
        essentials = self.essentials()
        essentials_dict = {
            "D": essentials[0],
            "B": essentials[1],
            "Mass per Metre": essentials[2],
            "t": essentials[3],
            "T": essentials[4],
            "r": essentials[5],
            "d": essentials[6],  # FIXME: indexing bug, check all modules
            "d_t": essentials[7],
            "b_T": essentials[8],
            "I_xx": essentials[9],
            "r_yy": essentials[10],
            "Z_xx": essentials[11],
            "S_xx": essentials[12],
            "u": essentials[13],
            "x": essentials[14],
            "Designation": essentials[15],
        }
        return essentials_dict

    def get_essentials_w_units(self):
        essentials = self.essentials()
        units = {
            "D": "mm",
            "B": "mm",
            "Mass per Metre": "kg/m",
            "t": "mm",
            "T": "mm",
            "r": "mm",
            "d": "mm",
            "d_t": "mm",
            "b_T": "mm",
            "I_xx": "cm^4",
            "r_yy": "cm",
            "Z_xx": "cm^3",
            "S_xx": "cm^3",
            "u": "",
            "x": "",
            "Designation": "",
        }

        # essentials_dict = {
        #     key: f"{value:.2f} {units[key]}"
        #     for key, value in zip(units.keys(), essentials)
        # }

        # """ # FIXME: try...
        essentials_dict = {
            key: (
                f"{value:.2f} {units[key]}"
                if isinstance(value, (int, float))
                else f"{value} {units[key]}"
            )
            for key, value in zip(units.keys(), essentials)
        }

        return essentials_dict


class SectionList:
    def __init__(self, sections: UniversalSection = None):
        if sections is None:
            sections = []
        self.sections = sections

    def __iter__(self):
        # * makes this object iterable
        return iter(self.sections)

    def __len__(self) -> int:
        return len(self.sections)

    def __str__(self) -> str:
        # return [for i in self: i.designation] #! erroneous
        return ", ".join([i.designation for i in self])

    @classmethod
    def by_Sxx(cls, min_Sxx: float | int, df=ub_df):
        """
        :return:
        """
        # TODO: note that the ub_df is defaulting to Universal Beam Data
        sections = []
        for designation, data in df.iterrows():
            # if data["S_xx"] >= min_Sxx: #! S_xx doesn't work, Sxx does
            if data["Sxx"] >= min_Sxx:
                section = UniversalSection.create(df, designation)
                sections.append(section)
        return cls(sections), [section.get_essentials() for section in sections]

    @classmethod
    def by_Zxx(cls, min_Zxx: float | int, df: DataFrame = ub_df):
        sections = []
        for designation, data in df.iterrows():
            # if data["Z_xx"] >= min_Zxx: #! S_xx doesn't work, Sxx does
            if data["Zxx"] >= min_Zxx:
                section = UniversalSection.create(df, designation)
                sections.append(section)
        return cls(sections), [section.get_essentials() for section in sections]


# class UniversalBeam(UniversalSection):
#     def __init__(self) -> None:
#         super().__init__()


# class UniversalColumn(UniversalSection):
#     def __init__(self) -> None:
#         super().__init__()


if __name__ == "__main__":
    # # Create a UniversalSection object by Designation
    # section_1016x305x584 = UniversalSection.create(ub_df, "1016x305x584")
    # print(section_1016x305x584.get_essentials())
    # print(section_1016x305x584)  # testing the __str__ method in the UniversalSection class; working ✅ # fmt: skip
    # print(section_1016x305x584.get_essentials_w_units())
    # # # Create multiple UniversalSection objects by SerialSize
    # sections_1016x305 = UniversalSection.create_serial_size(ub_df, "1016x305")
    # # print(sections_1016x305)

    # test_tuple = SectionList.create_by_Sxx(ub_df, 2320)
    # [print(i.designation) for i in test_tuple[0]]  #! discouraged for side-effects eg. printing # fmt: skip

    # print(test_tuple[1])
    list_a = SectionList.by_Zxx(2500)
    print(len(list_a[1]))
