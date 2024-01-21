import time
import numpy as np
import pandas as pd


class Spreadsheet:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.DataFrame({'Download Speed': []})
        self.df.to_excel(self.filename, index=False)

    def append_data(self, c1,c2=None,c3=None,c4=None,c5=None):
        self.df = pd.read_excel(self.filename)
        self.df = self.df.append({'Download Speed': c1}, ignore_index=True)
        self.df.to_excel(self.filename, index=False)