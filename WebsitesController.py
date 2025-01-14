"""
This section fill and submit forms in our websites.
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import gspread

from datetime import datetime
from random import randint

import EmailSender
import PageElements
import Setup
import sys
sys.path.append('/home/maor_animals_now_org/pytest')
import Autn


CHROMEDRIVER_PATH = Setup.CHROMEDRIVER_PATH

class webFunc:

    def __init__(self, site):
        self.site = site
        self.first_name = "testbot" + webFunc.random_char(3)
        self.last_name = webFunc.random_char(6)
        self.email = "test+bot"+ self.last_name + "@animals-now.org"
        self.phone = "067" + str(randint(1000000, 9999999))
        self.year_of_birth = ""
        self.info = [self.first_name, self.last_name, self.email, self.phone]
    def start_driver(self):
        """
        Determine and start the selenium webdriver.
        """
        chrome_options = Options()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080") 
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
    #    chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        #self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


    def url(self):
        """
        Navigate to the site address that accepted upon creating instance.
        """
        self.driver.execute_script("window.location = '{}'".format(self.site))

    @staticmethod
    def random_char(length):
        """
        Generate random alpha string, accept length of the string.
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        chars = ''
        for x in range(length):
            chars += chars.join(letters[randint(0, 25)])
        return chars

    def insert_info_to_field(self, field, keys):
        """
        The function find all element with <input> tag and search in each element for placeholder
        attribute. than check if any of placeholder_dict[field] is substring of placeholder value,
        if it does send keys to this element. If the function failed or succeed to send keys to this element,
        it will print massage to the console.
        accept:
        field - field to send keys
        keys - keys to send
        The function base on placeholder, if your form doesn't have placeholder,
        it won't work.
        """
        print('########### Trying to send keys to all "{}" input fields ###########'.format(field))
        # Find all elements with input tag (in the html <input>....</input>)
        input_elem_list = self.driver.find_elements_by_tag_name('input')

        # Number of input fields with placeholder that suitable to the given field we want to fil.
        appropriate_input_elem_found = 0
        num_of_fields_filled = 0
        for elem in input_elem_list:
            # Get the value of the placeholder inside input (<input>placeholder="some-value"</input>
            # Using try here because sometimes if you filled one input filled other can be remove.
            # And because we try to fill all appropriate input boxes there might be a chance that we now
            # try to get field(input box) that not exit anymore.
            try:
                real_placeholder = elem.get_attribute('placeholder')
            except:
                continue
            # If any of the item inside placeholder_dict[field] are also inside the real_placeholder,
            # it will send keys to this element(field).
            if any([plc in real_placeholder for plc in PageElements.PLACEHOLDER_DICT[field]]):
                appropriate_input_elem_found += 1
                try:
                    keys_status = self.send_keys_with_validation(elem, keys)
                    if keys_status:
                        print('Succeed to send keys to: "{}" (field placeholder).'.format(real_placeholder))
                        num_of_fields_filled += 1
                except:
                    pass
        print('Found {} {} input fields succeed to send keys to "{}" input fields'.format(appropriate_input_elem_found,
                                                                                        field,
                                                                                        num_of_fields_filled))
        if num_of_fields_filled == 0:
            error_msg = 'Failed to insert data to: "{}" field in form'.format(field)
            raise Exception(error_msg)


    def send_keys_with_validation(self, elem, keys):
        """
        Using selenium to send keys to input field on the website. After sending the keys to the input field, check if
        they arrived to there. if not, will try again. Maximum tries before failure 10 times.
        Accept:
        @elem - input field to send keys (selenium webpage element).
        @keys - keys to send (string)
        Return: True on success else False.
        Note:
        - Also in here we send char by char to the input box because sometimes the form don't accept your keys if you send
        them as long string.
        - We use this function to insert data to forms because sometimes we sent keys to input field but it doesn't get them.
        """
        maximum_tries = 10
        current_tries = 0
        text_in_input_box = ""
        while text_in_input_box != keys and current_tries < maximum_tries:
            elem.clear()
            for char in keys:
                elem.send_keys(char)
            text_in_input_box = elem.get_attribute('value')
            current_tries += 1
        if text_in_input_box == keys:
            return True
        return False

    ################## Challenge22, Etgar22 ##################
                    

    def close_move_to_english_website_pop_up(self):
        """
        On challenge22 ES sometimes there is pop up that ask the user to move to the english website,
        this method close this pop up.
        """
        pop_up_close_button = self.driver.find_element_by_css_selector(PageElements.MOVE_TO_EN_POP_UP_CLOSE_BUTTON_CSS_SELECTOR)
        pop_up_close_button.click()

    def send(self):
        """
        Click on "Submit/Continue" button in etgar22.co.il,in challenge22.com and in challenge22.com/es
        """
        send_button = self.driver.find_element_by_id(PageElements.CHALLENGES_FORM_SEND_BUTTON_ID)
        send_button.click()

    def etgarconfirm(self):
        """
        Click on "I accept the Term of use" check box in etgar22.co.il
        """
        confirm_checkbox = self.driver.find_element_by_xpath(PageElements.ACCEPT_TERM_CHECKBOX_XPATH)
        # this function (etgarconfirm) is used by several tests, in some it helps to scroll_into_view and in some it
        # fails the test (i.e Etgar22FormTest.py) scroll_into_view(self.driver, confirm_checkbox)
        confirm_checkbox.click()

    def ch_confirm_sixteen(self):
        """
        Click on "I am 16 or older and have read the Terms of Use" check box
        in challenge22.com and in challenge22.com/es
        """
        sixteen_checkbox = self.driver.find_element_by_xpath(PageElements.OLDER_THAN_16_CHECKBOX_XPATH)
        sixteen_checkbox.click()


    def teen_check_box(self):
        """
        Click on "I am less that 18 year old" check box in etgar22.co.il
        """
        
        teen_checkbox = self.driver.find_element_by_xpath(PageElements.TEEN_CHECKBOX_XPATH)
        teen_checkbox.click()
        
        
    def transferred_to_thank_you_page(self):
        """
        Check if the bot succeeded to submit the form (by checking if the bot in thank you page).
        """
        url = self.driver.current_url
        if "thank" not in url:
            print("Current Url: ", url)
            self.driver.quit()
            raise Exception("Did not transfer to thank you page.")
        print("Successfully transferred to thank you page.")            
################## Petitions ##################        
    def petitions_send(self):
        """
        Click on "Submit/Continue" button in animals-now.org's petitions
        """
        send_button = self.driver.find_element_by_css_selector(PageElements.PETITIONS_FORM_SEND_BUTTON_CSS_SELECTOR)
        # scrolling into view doesn't work in https://animals-now.org/investigations/turkey/?utm_source=test&utm_medium=test&utm_campaign=test
        # try it - open the console and type this:
        #   var elem = document.querySelector('div #form_petition-form button.frm_button_submit')
        #   elem.scrollIntoView(true);
        # scroll_into_view(self.driver, send_button)
        send_button.click()

    def add_my_name_to_petition(self):
        """
        Some of the times in some petition "add my name to petition" button appear before we can sign up
        to the petition, this function click on this button.
        REMOVE THIS FUNCTION WHEN THE A/B TEST IS DONE.
        """
        try:
            button = self.driver.find_element_by_css_selector(PageElements.ADD_MY_NAME_TO_PETITION_BUTTON_CSS_SELECTOR)
            button.click()
        except:
            print('Add my name to petition button not found, this button appear sometimes because its A/B test')


    def scroll_into_view(driver, element):
        print("scrolling into view element with id " + element.id)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def petitions_age(self):
        """
        Choose random birthday from the scroll in animals-now.org's petitions
        """
        if self.driver.find_element_by_xpath(PageElements.PETITION_HEBREW_AGE_BOX_XPATH):
            age_box = self.driver.find_element_by_xpath(PageElements.PETITION_HEBREW_AGE_BOX_XPATH)
        else:
            age_box = self.driver.find_element_by_xpath(PageElements.PETITION_ENGLISH_AGE_BOX_XPATH)

        age_box.click()
        select_age = self.driver.find_element_by_xpath(PageElements.PETITION_SELECT_AGE_SCROLL_BAR_XPATH.format(randint(1930, 2004)))
        select_age.click()
        self.year_of_birth = select_age
        
################## Check if sign up in sheets/gmail ##################        
     
    def check_in_sheets(self, sheet):
        """
        Some of the signed ups transfer to google sheet, this function check if the registration arrived to
        the google sheet. If it does, the registration delete from the google sheet.
        If the registration doesn't arrive to the google sheet, failure email will be sent to dev.
        Also there is a method that check if there only one row deleted from the google sheet, in case more or
        less then one row deleted the test failed and email sent to dev.
        Also write registration detail in google sheet named 'Report'(test@animals-now.org is the owner of this sheet)
        """
        client = Autn.get_service_sheet()  # open google sheet API client
        service = Autn.get_service_gmail()  # open gmail Api
        report_sheet = client.open("Report").sheet1  # open report sheet, will insert success or failure
        self.sheet = sheet

        row_failed_msg = "The bot submitted the form but the registration's information doesn't arrived to the" \
                         " suitable google sheet."
        row_success_all_msg = "Sign up succeed and removed from google sheet."
        row_remove_more_msg = "Sign up succeed but the bot removed more than one row in the google sheet. Means" \
                              "The bot may deleted from google sheet more than the test registration."
        row_not_remove_msg = "Sign up succeed but the bot failed to remove the test data from the google sheet."
        sign_up_sheet = client.open(self.sheet).sheet1  # open sign up form sheet
        time_now = str(datetime.today())[0:16]
        row_failed = [time_now, self.sheet, self.site, self.email, row_failed_msg]
        row_succeed_all = [time_now, self.sheet, self.site, self.email, row_success_all_msg]
        row_remove_more = [time_now, self.sheet, self.site, self.email, row_remove_more_msg]
        row_not_remove = [time_now, self.sheet, self.site, self.email, row_not_remove_msg]
        
        try:
            sign_up_sheet.find(self.email)  # search if the test email found in sign up form sheet
            rows_before_delete = len(sign_up_sheet.col_values(1))
            sign_up_sheet.delete_row(sign_up_sheet.find(self.email).row)
            rows_after_delete = len(sign_up_sheet.col_values(1))
            gap = str(rows_before_delete - rows_after_delete)
            row_failed.append(gap)  # adding the number of rows that remove
            row_succeed_all.append(gap)
            row_remove_more.append(gap)
            row_not_remove.append(gap)
            try:
                sign_up_sheet.find(self.email)  # try to find the test email again
                if rows_before_delete - rows_after_delete > 1:  # check if more then one row was delete
                    report_sheet.insert_row(row_remove_more, 2)  # report that more then one row was delete
                    report_sheet.insert_row(row_not_remove, 2)  # tell us the test email found after deleting
                    EmailSender.signup_failed_email(service,
                                                    row_remove_more)  # send email, open the func in order to see to who
                    EmailSender.signup_failed_email(service, row_not_remove)
                else:
                    report_sheet.insert_row(row_not_remove, 2)  # tell us the test email found after deleting
                    EmailSender.signup_failed_email(service, row_not_remove)
            except gspread.CellNotFound:
                if rows_before_delete - rows_after_delete > 1:  # check if more then one row was delete
                    report_sheet.insert_row(row_remove_more, 2)  # report that more then one row was delete
                    EmailSender.signup_failed_email(service, row_remove_more)
                else:
                    report_sheet.insert_row(row_succeed_all, 2)  # tell us that everything work right
        except gspread.CellNotFound:
            report_sheet.insert_row(row_failed, 2)  # tell us that test email didn't found in the sheet
            EmailSender.signup_failed_email(service, row_failed)


    def check_in_gmail(self, email_list, petitions_list):
        """
        When petition registration success, the user's details transfer to salesforce. if salesforce receive
        email with this form: test+???@animals-now.org, salesforce will send the user details to
        test@animals-now.org.
        This function search in test@animals-now.org inbox for email from saleforce
        with the user's details, if the email not found the test failed and email about the failure will be send.
        Also write registration detail in google sheet named 'Report'(test@animals-now.org is the owner of this sheet)
        accept:
        email_list - list of email that the bot used to sign ups.
        petitions_list - list of petitions url the bot signed up.
        """
        service = Autn.get_service_gmail()  # open gmail API client
        client = Autn.get_service_sheet()  # open google sheet API client
        report_sheet = client.open("Report").sheet1  # open report sheet, will insert success or failure

        petitions_index = 0
        for email_address in email_list:
            num_emails_received = EmailSender.petition_emails(service, 'me', email_address)
            if num_emails_received == 1:
                status = "Succeed! Salesforce email received"
            else:
                status = "Failed - Found " + str(num_emails_received) + " emails instead of 1"
            row_status = [str(datetime.today())[0:16], "Petition", petitions_list[petitions_index], email_address, status]
            report_sheet.insert_row(row_status, 2)
            if num_emails_received != 1:
                EmailSender.signup_failed_email(service, row_status)
            petitions_index += 1

#     def healthissue(self):
#         """
#         Sign ups to challenges's websites with random health.
#         OLD FUNCTION CHECK IT BEFORE USING!!!
#         """
#         etgar = "https://etgar22.co.il/?utm_source=test&utm_medium=test&utm_campaign=test"
#         ch = "https://challenge22.com/?utm_source=test&utm_medium=test&utm_campaign=test"
#         ch_es = "https://challenge22.com/es/?utm_source=test&utm_medium=test&utm_campaign=test"
#         if self.site == etgar:
#             general_issues_checkbox = self.driver.find_element_by_xpath('//label[@id="tfa_164-L"]')
#             general_issues_checkbox.click()
#             facebook_placeholder = "שם מלא ושם בפייסבוק"
#         elif self.site == ch:
#             general_issues_checkbox = self.driver.find_element_by_xpath('//label[@id="tfa_91-L"]')
#             general_issues_checkbox.click()
#             facebook_placeholder = "Full Name & Facebook Name"
#         elif self.site == ch_es:
#             general_issues_checkbox = self.driver.find_element_by_xpath('//label[@id="tfa_91-L"]')
#             general_issues_checkbox.click()
#             facebook_placeholder = "Nombre completo y nombre en Facebook"

#         self.send()
#         health_issues_id = ["tfa_96-L", "tfa_97-L", "tfa_98-L", "tfa_101-L", "tfa_102-L"]
#         random_issue = random.choice(health_issues_id)
#         specific_issues_checkbox = self.driver.find_element_by_xpath(
#             '//label[@class="label postField"][@id="{}"]'.format(random_issue))
#         specific_issues_checkbox.click()
#         sleep(1)

#         if random_issue == "tfa_97-L":  # "עברת ניתוח בריאטרי"
#             time_pass_id = ["tfa_114-L", "tfa_113-L", "tfa_114-L"]
#             random_time_pass = random.choice(time_pass_id)
#             time_pass_checkbox = self.driver.find_element_by_xpath(
#                 '//label[@id="{}"]'.format(random_time_pass))
#             time_pass_checkbox.click()
#             if random_time_pass == "tfa_113-L":  # "מעל שנה (ללא סיבוכים מיוחדים)"
#                 pass
#             else:  # "עד שנה, מעל שנה (עם סיבוכים מיוחדים)"
#                 facebook_name_box = self.driver.find_elements_by_xpath(
#                     '//input[@placeholder = "{}"]'.format(facebook_placeholder))
#                 for box in facebook_name_box:
#                     try:
#                         box.send_keys("test+bot" + "bodek")
#                     except:
#                         pass
#         else:  # "כל שאר המחלות"
#             try:
#                 facebook_name_box = self.driver.find_elements_by_xpath(
#                     '//input[@placeholder = "{}"]'.format(facebook_placeholder))
#                 for box in facebook_name_box:
#                     try:
#                         box.send_keys("test+bot" + "bodek")
#                     except:
#                         pass
#             except:
#                 pass

#     def petitions_age(self):
#         """
#         Choose random birthday from the scroll in animals-now.org's petitions
#         """
#         age_box = self.driver.find_element_by_xpath('//select[@placeholder="שנת לידה"]')
#         age_box.click()
#         select_age = self.driver.find_element_by_xpath('//option[@value="{}"]'.format(randint(1930, 2004)))
#         select_age.click()
