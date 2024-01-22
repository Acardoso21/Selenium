from csv_interface import CsvWriter
headers=['header1', 'header2', 'header3']
test = CsvWriter("testingfile.csv", headers)
test.append_data("data_append")