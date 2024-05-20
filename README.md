# STEEL COLUMN DESIGN

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
<!-- ![Postgres]() ...coming soon -->

- BS 5950-1:2000 and EN 1993-1-1:2005

- Jupyter notebooks using [handcalcs](https://github.com/connorferster/handcalcs) and [forallpeople](https://connorferster.github.io/forallpeople/index.html)
- `handcalcs` - render Python calculation code automatically in Latex how one might format their calculation by hand: write the symbolic formula, followed by numeric substitutions, and then the result.
- `forallpeople` - a Python library for representing the SI base units to enable easy-to-use, units-aware calculations. Also incl. US Customary Units
- Crash course on how to use both on YouTube:
  - [Introduction to handcalcs: Absolute Beginners Guide](https://youtu.be/ZNFhLCWqA_g?feature=shared)
  - [Engineering Calculations: Handcalcs-on-Jupyter vs. Excel](https://youtu.be/n9Uzy3Eb-XI?feature=shared)
  -

## Notebooks `.ipynb`

1. Starter Notebook [0](/0-starter.ipynb)
2. Struts [1](/struts.ipynb)
3. Beam-Columns [2](/beam_col.ipynb)

## 📝 in a `.ipynb` means the value should be edited

- probably a manual calc, read from a table, or not coded

## Setup

```bash
# Create virtualenv using bash
python3 -m pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Etc

- [Greek symbols](https://github.com/connorferster/handcalcs?tab=readme-ov-file#greek-symbols)
- [TeX code, without the render](https://github.com/connorferster/handcalcs?tab=readme-ov-file#greek-symbols)
- [Handcalcs for scripts i.e as a `@decorator`](https://github.com/connorferster/handcalcs?tab=readme-ov-file#basic-usage-2-as-a-decorator-on-your-functions-handcalc)
- [Pint: make units easy](https://pint.readthedocs.io/en/stable/)
