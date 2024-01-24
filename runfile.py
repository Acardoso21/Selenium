import sys
sys.path.append('csvInterface')
from csvInterface.csv_interface import CsvWriter
sys.path.append('selenium_scripts')
from selenium_scripts.selenium_interface import SeleniumInterface

# gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
# down, up, j, p = gfibertest.run_google_fiber_test()
# print(down)
# print(up)
# print(j)
# print(p)
# gdata = [down, up, p, j]
headers = ['download speed','upload speed','jitter','ping']
table = CsvWriter("googlefibertest1",headers)
# table.append_data(gdata)
speedcom = SeleniumInterface('https://www.speedtest.net/')
down, up, j, p =speedcom.run_speedtest_NET()
netdata = [down, up, p, j]
table.append_data(netdata)

# <button class="close-btn pure-button pure-button-primary">Close</button>

# <div class="modal modal-in-place celebration-modal" role="alertdialog" style="display: block;">
#   <a href="#" class="notification-dismiss close-btn" title="Dismiss" role="button"></a>
#   <div class="pure-u-1 u-align-center u-c">
#     <div aria-label="50 billion speedtests celebration modal">
#       <div aria-hidden="true">
#           <lottie-player src="/images/50b-anim-4.json" background="transparent" speed="1" loop="" autoplay=""></lottie-player>
#       </div>
#     </div>
#     <p>You did it! Thank you for helping us reach 50 billion Speedtest results! <a href="https://www.ookla.com/articles/speedtest-50-billion" target="_blank">Read more</a>.</p>
#     <p><button class="close-btn pure-button pure-button-primary">Close</button></p>
#   </div>
# </div>