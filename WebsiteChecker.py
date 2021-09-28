import customFunc
import emailfunc
import requests
from requests.exceptions import ConnectionError
import random
import time

# If you add a website, also add it in the error_status.json that located in the server(look in Setup.py for it's path)
fish = "https://fish.org.il/"
etgar = "https://etgar22.co.il/"
ch = "https://challenge22.com/"
animals = "https://animals-now.org/"
anonymous = "https://anonymous.org.il/"
veg = 'https://veg.co.il/'
live_act = 'https://liveact.org/'
videos = 'https://videos.animals-now.org/'
salmon = 'https://salmon.org.il/'
animal = 'https://animal.org.il/'
rifq = 'https://rifq.org/'
students = 'https://animals-students.co.il/'
chicken = 'https://chicken.org.il/'
tnuva = 'https://tnuvacruelty.co.il/'
share = 'https://sharetheworld.org.il/'
cage = 'https://cagefree.co.il/'
behemla = 'https://www.behemla.org.il/'
haywan = 'https://hayawan.org/'
quizzes = 'https://quizzes.anonymous.org.il/'
shira = 'https://shirahertzanu.com/'

# website to check
site_list = [etgar, ch, animals, anonymous, veg, live_act, fish, videos, salmon, animal, rifq,
             students, chicken, tnuva, share, cage, behemla, haywan, quizzes, shira]

# Header for the get request
header_list = [
 {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like '
                'Gecko) Chrome/28.0.1464.0 Safari/537.36'},
 {'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 '
                'Firefox/63.0'},
 {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like '
                'Gecko) Chrome/41.0.2228.0 Safari/537.36'},
 {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'},
 {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 '
                'Firefox/5.0 Opera 11.11'},
 {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; '
                'Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)'},
 {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.59.12) '
                'Gecko/20160044 Firefox/52.59.12'},
 {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'},
 {'User-Agent': 'Mozilla/5.0 (X11;  Ubuntu; Linux i686; rv:52.0) '
                'Gecko/20100101 Firefox/52.0'},
 {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like '
                'Gecko) Chrome/35.0.2309.372 Safari/537.36'},
 {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                'like Gecko) Chrome/33.0.1750.517 Safari/537.36'}]


GET_REQUEST_OK_CODE = 200
# If it took the website more then this constant to respond it declared as error
GET_REQUEST_MAX_WAIT_SECONDS = 60
# How many times to try the test before declared it as failure
TRIES_BEFORE_FAILURE = 3
SECONDS_TO_WAIT_BETWEEN_TRIES = 8

# This messages will be sent in emails when error occur.
GET_REQUEST_CODE_ERROR_MSG = 'Website returned code error number: {}\n' \
                             'If you not familiar with this code error please google it,' \
                             'also please make sure the website working well.'
CONNECTION_ERROR_MSG = 'Get request sent but the website does not respond\n' \
                       'That means the website does not loaded when the bot tried to open it\n' \
                       'Please go to the website and make sure it open as it suppose to.'
TOO_MUCH_TIME_TO_LOAD_MSG = 'The website took too much time to load - : {} seconds\n' \
                            'Please go to the website and make sure it open fast.'
FAMILIAR_WORD_ERROR_MSG = 'The word "animals" does not found in the page source\n' \
                          'Which means the website might be cracked.\n' \
                          'Please go to the website and make sure it fine.'
GIBBERISH_ERROR_MSG = 'Gibberish character("×") found in the page\n' \
                      'Please go to the website and make sure it fine.'

# This messages will be print to the console in order to help us debug problems
PRINT_TO_CONSOLE_CODE_ERROR_FAIL_MSG = 'Website: {}, get request code error: {}, fail number: {}'
PRINT_TO_CONSOLE_CONNECTION_ERROR_FAIL_MSG = 'Website: {}, connection error, fail number: {}'
PRINT_TO_CONSOLE_TOO_MUCH_TIME_TO_LOAD_MSG = 'Website: {}, time took to load: {}, fail number: {}'
PRINT_TO_CONSOLE_FAMILIAR_WORD_ERROR_MSG = 'Website: {}, the familiar word was not found in the page'
PRINT_TO_CONSOLE_GIBBERISH_ERROR_MSG = 'Website: {}, Gibberish character("×") found in the page'


def test_get_request(site, failure_dict, header):
    """
    Send get request to the site and check to status code and the connection.
    if there is a problem try again up to the maximum tries(TRIES_BEFORE_FAILURE).
    When reach to the maximum tries will change in the failure dictionary the suitable error status to true
    and add the corresponding error message.
    """
    failure_counter = 0
    failure_status = True
    while failure_counter < TRIES_BEFORE_FAILURE and failure_status:
        try:
            request = requests.get(site, headers=header)
            if request.status_code == GET_REQUEST_OK_CODE:
                failure_status = False
                continue
            else:
                failure_counter += 1
                print(PRINT_TO_CONSOLE_CODE_ERROR_FAIL_MSG.format(site, request.status_code, failure_counter))
                if failure_counter >= TRIES_BEFORE_FAILURE:
                    failure_dict['CodeError'][0] = True
                    failure_dict['CodeError'][1] = GET_REQUEST_CODE_ERROR_MSG.format(str(request.status_code))
        except ConnectionError:
            failure_counter += 1
            print(PRINT_TO_CONSOLE_CONNECTION_ERROR_FAIL_MSG.format(site, failure_counter))
            if failure_counter >= TRIES_BEFORE_FAILURE:
                failure_dict["ConnectionError"][0] = True
                failure_dict["ConnectionError"][1] = CONNECTION_ERROR_MSG
        customFunc.sleep(SECONDS_TO_WAIT_BETWEEN_TRIES)


def test_get_request_respond_time(site, failure_dict, header):
    """
    Check how much second it take the website to respond to get request.
    if there is a problem try again up to the maximum tries(TRIES_BEFORE_FAILURE).
    When reach to the maximum tries will change in the failure dictionary the LoadTimeError status to true
    and add the time its took the website to respond.
    """
    failure_counter = 0
    failure_status = True
    while failure_counter < TRIES_BEFORE_FAILURE and failure_status:
        start = time.time()
        try:
            request = requests.get(site, headers=header)
        except:
            return
        end = time.time()
        if end - start > GET_REQUEST_MAX_WAIT_SECONDS:
            failure_counter += 1
            print(PRINT_TO_CONSOLE_TOO_MUCH_TIME_TO_LOAD_MSG.format(site, str(end - start)[0:4], failure_counter))
            if failure_counter >= TRIES_BEFORE_FAILURE:
                failure_dict["LoadTimeError"][0] = True
                failure_dict["LoadTimeError"][1] = TOO_MUCH_TIME_TO_LOAD_MSG.format(str(end - start)[0:4])
        else:
            failure_status = False
            continue
        customFunc.sleep(SECONDS_TO_WAIT_BETWEEN_TRIES)


def test_familiar_word_and_gibberish(site, failure_dict, header):
    """
    Search for familiar words in the page, if not found - Fail.
    In all of the sites besides animal, behemla and haywan - we have the word animals in the source code.
    in animal site there's animal word and in behemla site there's behemla word and in haywan site there's
    haywan word in their source code. So with those word we test those specific sites.
    We use this test in order to make sure our website didn't cracked.

    Also we test here for gibberish character. Because problems with the website's cash can cause to all
    characters in the website to become gibberish.
    """
    try:
        request = requests.get(site, headers=header)
    except:
        return
    page = request.text  # get the page source code
    if 'animal' not in page and 'behemla' not in page and 'hayawan' not in page:
        print(PRINT_TO_CONSOLE_FAMILIAR_WORD_ERROR_MSG.format(site))
        failure_dict["FamiliarWordError"][0] = True
        failure_dict["FamiliarWordError"][1] = FAMILIAR_WORD_ERROR_MSG

    # Search for character that always appear in gibberish text, if found - Fail
    if '×' in page:
        print(PRINT_TO_CONSOLE_GIBBERISH_ERROR_MSG.format(site))
        failure_dict["GibberishError"][0] = True
        failure_dict["GibberishError"][1] = GIBBERISH_ERROR_MSG



def send_emails_on_failure(site, failure_dict, header, service):
    """
    Sends emails on each failure, send only if the website's counter in error_status.json is set to 0.
    If email sent it change the counter to WEBSITE_CHECKER_EMAILS_SESSION_DELAY(const in emailfunc file).
    If email was not send it decrease the counter by 1.
    """
    if failure_dict["CodeError"][0]:
        emailfunc.web_error_email('CodeError', service, failure_dict["CodeError"][1], site, str(header))
    else:
        emailfunc.reset_error_counter('CodeError', service, site)

    if failure_dict["ConnectionError"][0]:
        emailfunc.web_error_email('ConnectionError', service, failure_dict["ConnectionError"][1], site, str(header))
    else:
        emailfunc.reset_error_counter('ConnectionError', service, site)

    if failure_dict["LoadTimeError"][0]:
        emailfunc.web_error_email('LoadTimeError', service, failure_dict["LoadTimeError"][1], site, str(header))
    else:
        emailfunc.reset_error_counter('LoadTimeError', service, site)

    if failure_dict["FamiliarWordError"][0]:
        emailfunc.web_error_email('FamiliarWordError', service, failure_dict["FamiliarWordError"][1], site, str(header))
    else:
        emailfunc.reset_error_counter('FamiliarWordError', service, site)

    if failure_dict["GibberishError"][0]:
        emailfunc.web_error_email('GibberishError', service, failure_dict["GibberishError"][1], site, str(header))
    else:
        emailfunc.reset_error_counter('GibberishError', service, site)


def test_run():
    service = customFunc.auth.get_service_gmail()
    for site in site_list:
        header = random.choice(header_list)
        failure_dict = {"CodeError": [False, ''],
                        "ConnectionError": [False, ''],
                        "LoadTimeError": [False, ''],
                        "FamiliarWordError": [False, ''],
                        "GibberishError": [False, '']}
        test_get_request(site, failure_dict, header)
        test_get_request_respond_time(site, failure_dict, header)
        test_familiar_word_and_gibberish(site, failure_dict, header)
        send_emails_on_failure(site, failure_dict, header, service)
        customFunc.sleep(1)

test_run()
