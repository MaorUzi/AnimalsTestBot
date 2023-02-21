from .. import WebsitesController, Setup

site = "https://etgar22.co.il/?utm_source=test&utm_medium=test&utm_campaign=test"
sheet = "אתגר 22 נוער - 2019 (Responses)"

session = WebsitesController.webFunc(site)
session.start_driver()
session.url()
WebsitesController.sleep(10)
session.insert_info_to_field('FullName', session.first_name + ' ' + session.last_name)
session.insert_info_to_field('Email', session.email)
session.insert_info_to_field('Phone', session.phone)
session.etgarconfirm()
session.teen_check_box()
session.send()
age = str(WebsitesController.randint(14, 17))
parent_phone = "067" + str(WebsitesController.randint(1000000, 9999999))
WebsitesController.sleep(6)
session.insert_info_to_field('Age', age)
session.send()
WebsitesController.sleep(3)
session.insert_info_to_field('Phone', parent_phone)
WebsitesController.sleep(5)
session.send()
WebsitesController.sleep(10)
session.transferred_to_thank_you_page()
session.driver.quit()

WebsitesController.sleep(600)
session.check_in_sheets(sheet)
