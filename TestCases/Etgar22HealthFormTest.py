from .. import WebsitesController, Setup

site = "https://etgar22.co.il/?utm_source=test&utm_medium=test&utm_campaign=test"
sheet = "אתגר 22 מבוגרים - 2019 (Responses)"

session = WebsitesController.webFunc(site)
session.url()
WebsitesController.sleep(6)
session.insertinfo()
session.etgarconfirm()
session.healthissue()
session.send()
session.driver.quit()

WebsitesController.sleep(480)
session.check_in_sheets(sheet)

client = WebsitesController.Autn.get_service_sheet()  # addindg to form name in the report "health issue" because etgar22 and
report_sheet = client.open("Report").sheet1  # etgar22 healh issue have the same form
time_now = str(WebsitesController.datetime.today())[0:16]
report_sheet.update_cell(report_sheet.find(session.info[2]).row, report_sheet.find(session.info[2]).col-1, (sheet +" - health issue"))
