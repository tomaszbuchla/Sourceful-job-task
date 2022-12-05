class contactPage():
    # test data
    adress = 'https://sourceful.nl/nl/contact-pl/'
    name = "testName testSurname"
    mail = "test@mail.com"
    # Locators
    cookieForm = 'cookie-law-btn'
    nameForm = 'your-name'
    mailForm = 'wpcf7-email'
    buttonForm = 'wpcf7-submit'
    confirmForm = 'wpcf7-response-output'

    expectedPositiveOutput = 'Dziękujemy, wiadomość została wysłana.'