import sys
sys.path.append('csvInterface\csv_interface.py')
from csvInterface.csv_interface import CsvWriter
from selenium_interface import SeleniumInterface

gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
down, up, j, p = gfibertest.run_google_fiber_test()
print(down)
print(up)
print(j)
print(p)
gdata = [down, up, p, j]
headers = ['download speed','upload speed','jitter','ping']
table = CsvWriter("googlefibertest1",headers)
table.append_data(gdata)
