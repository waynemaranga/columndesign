import pandas as pd
import os
import json
from collections import OrderedDict

## --> OS
# -- Get excel file
cwd = os.getcwd()  # get current working directory
# print(cwd)
dir_list = os.listdir(cwd)  # list files and dir. in current working dir.
# print(dir_list)
# testsheetfilepath = "/test/uc_bs5950_datasheet.xlsx"
testsheetfilepath = "/test/uc_datasheet_ec3.xlsx"
file_path = os.path.join(cwd + testsheetfilepath)
# print(file_path)  # * working
if not os.path.exists("db"):
    # ... checks it in os.listdir of cwd
    # print(True) # testing when if not was if
    os.makedirs("db")

ub_df = pd.read_excel(
    file_path, sheet_name="datasheet", header=0
)  # Read spreadsheet into Pandas DataFrame
#   ... header=0 makes the first row the headers, so using Excel tables isn't necessary # fmt: skip
# print(ub_df)
# print(ub_df.columns)
ub_df["Additional"] = ub_df["Additional"].apply(
    lambda x: False if pd.isnull(x) else True
)
#   ... if the cell is empty, append False, else True i.e it's additional
# print(ub_df)

ub_df["Designation"] = ub_df.apply(
    lambda row: str(row[0]) + str(row[1]), axis=1
)  # for each row in the 'Designation' index, apply a concat. of the first and second row in the df, using axis arg to specify apply fn. along rows
# ... axis applys function along an axis if the DataFrame; 0 for index, 1 for row axis
# print(ub_df)
ub_df["Designation"] = ub_df["Designation"].str.replace(" ", "")  # trim whitespace
# print(ub_df)
ub_df["SerialSize"] = ub_df["SerialSize"].str.replace(" ", "")
# ub_df["MassMarker"] = ub_df["MassMarker"].str.replace(" ", "") # redundant, dropped
ub_df.drop(ub_df.columns[1], axis=1, inplace=True)
# print(ub_df)
designation = ub_df.pop("Designation")  # Remove the 'section' column
ub_df.insert(0, "Designation", designation)  # Insert 'section' column at the beginning
# print(ub_df)


def universal_json(dataframe, json_file):
    json_object = {}
    for (idx,row) in (dataframe.iterrows()):  # fmt: skip
        # idx shows not accessed by Pylance, but necessary to unpack dataframe.iterrows() return value which is a tuple # see docs
        designation = row["Designation"]
        section_data = OrderedDict()  # using ordered dictionary to move Designation key to first item # fmt: skip
        for col in dataframe.columns:
            if col != "Designation":
                section_data[col] = row[col]

        section_data["Designation"] = designation
        section_data.move_to_end("Designation", last=False)  # last=False moves Designation row to beginning # fmt: skip
        json_object[designation] = section_data

    with open(os.path.join("db", json_file), "w") as file:
        json.dump(json_object, file, indent=4)


if __name__ == "__main__":
    universal_json(ub_df, "uc_en10365.json")  # FIXME: re-writelib, for uc
