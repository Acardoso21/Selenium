from selenium_interface import SeleniumInterface
from spreadsheet import Spreadsheet

gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
table = Spreadsheet('speed_test_results.xlsx')
down, up, p, j = gfibertest.run_google_fiber_test()

table.append_data(down,up,p,j)
