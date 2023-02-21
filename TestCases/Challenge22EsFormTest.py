from .. import WebsitesController, Setup

UTM_TEST = Setup.UTM_TEST

site = "https://challenge22.com/es/?utm_source=test&utm_medium=test&utm_campaign=test&test={}".format(UTM_TEST)
sheet = "הרשמה לאתגר 22 - SPANISH"

session = WebsitesController.webFunc(site)
session.start_driver()
session.url()
WebsitesController.sleep(10)
try:
  session.close_move_to_english_website_pop_up()
except:
  print("Didn't close move to english website")
session.insert_info_to_field('FullName', session.first_name + ' ' + session.last_name)
session.insert_info_to_field('Email', session.email)
session.ch_confirm_sixteen()
WebsitesController.sleep(5)
session.send()
WebsitesController.sleep(10)
session.transferred_to_thank_you_page()
session.driver.quit()

WebsitesController.sleep(600)
session.check_in_sheets(sheet)
