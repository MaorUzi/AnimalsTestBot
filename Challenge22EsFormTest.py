import customFunc
import Setup

UTM_TEST = Setup.UTM_TEST

site = "https://challenge22.com/es/?utm_source=test&utm_medium=test&utm_campaign=test&test={}".format(UTM_TEST)
sheet = "הרשמה לאתגר 22 - SPANISH"

session = customFunc.webFunc(site)
session.start_driver()
session.url()
customFunc.sleep(10)
session.insert_info_to_field('FirstName', session.first_name)
session.insert_info_to_field('LastName', session.last_name)
session.insert_info_to_field('Email', session.email)
session.ch_confirm_sixteen()
customFunc.sleep(5)
session.send()
customFunc.sleep(10)
session.transferred_to_thank_you_page()
session.driver.quit()

customFunc.sleep(600)
session.check_in_sheets(sheet)
