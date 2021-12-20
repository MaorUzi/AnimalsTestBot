PLACEHOLDER_DICT = {'FirstName': ['פרטי', 'First', 'first', 'Nombre', 'nombre'],
                    'LastName': ['משפחה', 'Last', 'last', 'Apellido', 'apellido'],
                    'Email': ['אימייל', 'מייל', 'דוא"ל', 'דואר אלקטרוני', "דוא'ל", 'Email', 'email',
                              'Correo electrónico', 'correo electrónico'],
                    'Phone': ['טלפון', 'נייד', 'Phone', 'phone', 'Mobile', 'mobile', 'Teléfono', 'teléfono',
                              'Móvil', 'móvil'],
                    'Age': ['גיל', 'Age', 'age', 'Años', 'años'],
                    'Birthday': ['שנת לידה', 'Birthday', 'birthday', 'Year', 'year', 'Cumpleaños', 'cumpleaños'],
                    'FullName': ['שם מלא', 'שם', 'Full name', 'full name', 'Name', 'name',
                                 'Nombre completo', 'nombre completo', 'Nombre', 'nombre'],
                    }



################# Etgar22, Challenge22 English, Challenge22 ES #################

"""
Sometimes on challenge22.com/es there is a pop up that ask the user to move to the english website,
this element is the close button of this pop up.
"""
MOVE_TO_EN_POP_UP_CLOSE_BUTTON_CSS_SELECTOR = "body > div.mfp-wrap.mfp-close-btn-in.mfp-auto-cursor.alternate-version-" \
                                   "popup-container.mfp-ready > div > div.mfp-content > div > button"

"""
ID of the send button(the button to finnish the registration) in etgar22.co.il,in challenge22.com 
and in challenge22.com/es
"""

CHALLENGES_FORM_SEND_BUTTON_ID = 'tfa_148'

"""
xPath of "I accept the Term of use" check box in etgar22.co.il
"""

ACCEPT_TERM_CHECKBOX_XPATH = '//label[@id="tfa_168-L"]'


"""
xPath of "I am 16 or older and have read the Terms of Use" check box in challenge22.com and in challenge22.com/es
"""

OLDER_THAN_16_CHECKBOX_XPATH = '//label[@id="tfa_93-L"]'

"""
xPath of "מסלול הנוער" check box in etgar22.co.il
"""

TEEN_CHECKBOX_XPATH = '//label[@for="youth-age-group_0"]'


####################### Animals Petitions #######################


"""
"Submit/Continue" button in animals-now.org's petitions
"""

PETITIONS_FORM_SEND_BUTTON_CSS_SELECTOR = 'div #form_petition-form button.frm_button_submit'

"""
Sometimes in some petition "add my name to petition" button appear before we can sign up this is the css selector
of the button
"""

ADD_MY_NAME_TO_PETITION_BUTTON_CSS_SELECTOR = 'div.add-me-to-petition-button a.fl-button'

"""
xPath of Hebrew age check box in animals-now.org petitions
"""
PETITION_HEBREW_AGE_BOX_XPATH = '//select[@placeholder="שנת לידה"]'

"""
xPath of English age check box in animals-now.org petitions
"""
PETITION_ENGLISH_AGE_BOX_XPATH = '//select[@placeholder="Year of Birth"]'


"""
xPath of select age scroll bar in animals-now.org petitions. 
"""
PETITION_SELECT_AGE_SCROLL_BAR_XPATH = '//option[@value="{}"]'
