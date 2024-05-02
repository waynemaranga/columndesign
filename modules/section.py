import pandas as pd
import os

uc_json = os.path.join(os.getcwd() + "/db/uc_bs5950.json")
uc_df = pd.read_json(uc_json, orient="index")


class UniversalColumn:
    def __init__(self, designation):
        data = uc_df.loc[designation]

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

    def __str__(self) -> str:
        return f"{self.designation}"

    @staticmethod
    def create(designation):
        """Create column section by section designation"""
        return UniversalColumn(designation)


class SectionList:
    def __init__(self, sections: UniversalColumn = None):
        if sections is None:
            sections = []
        self.sections = sections

    def __iter__(self):
        # * makes this object iterable
        return iter(self.sections)

    def __len__(self) -> int:
        return len(self.sections)

    def __str__(self) -> str:
        return ", ".join([i.designation for i in self])


if __name__ == "__main__":
    ...
