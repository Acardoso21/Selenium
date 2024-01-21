import pandas as pd

class Spreadsheet:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.DataFrame({'Download Speed': []})
        self.df.to_excel(self.filename, index=False)

    def append_data(self, data):
        self.df = pd.read_excel(self.filename)
        self.df = self.df.append({'Download Speed': data}, ignore_index=True)
        self.df.to_excel(self.filename, index=False)