import csv
from datetime import datetime

class CsvWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        # write the headers to the CSV file
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + self.headers)

    def append_data(self, data):
        if not isinstance(data, list):
            data = [data]

        # append data to the CSV file
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + data)
