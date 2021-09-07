import customFunc

site = "https://veg.co.il/challenge22/?utm_source=test&utm_medium=test&utm_campaign=test"
sheet = "אתגר 22 מבוגרים - 2019 (Responses)"
sheet1 = "אתגר 22 - טלפניות (Responses)"

session = customFunc.webFunc(site)
session.start_driver()
session.url()
customFunc.sleep(10)
session.insert_info_to_field('FirstName', session.first_name)
session.insert_info_to_field('LastName', session.last_name)
session.insert_info_to_field('Email', session.email)
session.insert_info_to_field('Phone', session.phone)
session.etgarconfirm()
customFunc.sleep(5)
session.send()
customFunc.sleep(10)
session.transferred_to_thank_you_page()
session.driver.quit()

customFunc.sleep(600)
session.check_in_sheets(sheet)
session.check_in_sheets(sheet1)
