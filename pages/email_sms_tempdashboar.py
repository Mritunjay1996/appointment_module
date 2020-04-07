from selenium.webdriver.common.by import By
import allure


class emailsmsdashbObj:
    logo = (By.XPATH, "//img[@class='logo-image-container sizing']")
    profileImg = (By.XPATH, "//img[@class='img-circle img-cu stom min-image-size sizeHeight']")
    profileName = (By.XPATH, "//span[@class='user-name-container']")
    profileDrpdwn = (By.XPATH, "//i[@class='fa fa-angle-down leftSp ace']")
    myProfile = (By.XPATH, "//a[contains(text(),'Mijn profiel')]")
    language = (By.XPATH, "//a[contains(text(),'Taal')]")
    logout = (By.XPATH, "//a[contains(text(),'Log Out')]")
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    labelEmail = (By.XPATH, "//h1[@class='title-4']")
    personalSign = (By.XPATH, "//div[@class='action']/div[1]/a[1]")
    teamSign = (By.XPATH, "//div[@class='app-head']//div[2]//a[1]")
    newTemplate = (By.XPATH, "//a[@class='btn blue app-data line']")
    initialAppoint = (By.XPATH, "//a[contains(text(),'Eerste afspraak')]")
    appointmentCnfrm = (By.XPATH, "//a[contains(text(),'Afspraak bevestiging')]")
    appointmentReminder = (By.XPATH, "//a[contains(text(),'Herinnering')]")
    rescheduling = (By.XPATH, "//a[contains(text(),'Afspraak verzetten')]")
    cancellation = (By.XPATH, "//a[contains(text(),'Annuleren')]")
    emailTemplate = (By.XPATH, "//h2[contains(text(),'E-mail Template')]")
    smsTemplate = (By.XPATH, "//h2[contains(text(),'SMS-sjabloon')]")
    saveBtn = (By.XPATH, "//button[@class='btn blue']")
    previewBtn = (By.XPATH, "//a[contains(text(),'Voorbeeld')]")
    defaultTemp = (By.XPATH, "//a[contains(text(),'Gebruik standaardtemplate')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify Logo on Email & SMS Template Dashboard Page')
    def verifycalendarLogo(self):
        return self.browser.find_element(*self.logo).is_displayed()

    @allure.step('Verify Recruiter profile image on Email & SMS Template Dashboard Page')
    def verifyProfileimage(self):
        return self.browser.find_element(*self.profileImg).is_displayed()

    @allure.step('Verify Recruiter profile name on Email & SMS Template Dashboard Page')
    def verifyProfilename(self):
        return self.browser.find_element(*self.profileName).text

    @allure.step('Verify My profile option in recruiter profile dropdown on Email & SMS Template Dashboard Page')
    def verifydropdownoption1(self):
        self.browser.find_element(*self.profileDrpdwn).click()
        return self.browser.find_element(*self.myProfile).text

    @allure.step('Verify My profile option in recruiter profile dropdown on Email & SMS Template Dashboard Page')
    def verifydropdownoption2(self):
        return self.browser.find_element(*self.language).text

    @allure.step('Verify Log out option in recruiter profile dropdown on Email & SMS Template Dashboard Page')
    def verifydrpodownoption3(self):
        return self.browser.find_element(*self.logout).text

    @allure.step('Verify Appointment tab on Email & SMS Template Dashboard Page')
    def verifyappTab(self):
        return self.browser.find_element(*self.appointmentTab).is_displayed()

    @allure.step('Verify Label for Agenda on Email & SMS Template Dashboard Page')
    def verifyEmailSmsLabel(self):
        return self.browser.find_element(*self.labelEmail).text

    @allure.step('Verify Personal Signature Button ')
    def verifyPersonalSignBtn(self):
        return self.browser.find_element(*self.personalSign).is_displayed()

    @allure.step('Verify Team Signature Button ')
    def verifyTeamSignatireBtn(self):
        return self.browser.find_element(*self.teamSign).is_displayed()

    @allure.step('Verify New Template Button ')
    def verifyNewtemplateBtn(self):
        return self.browser.find_element(*self.newTemplate).is_displayed()

    @allure.step('Verify Initial Appointment Schedule tab ')
    def verifyInitialapntmnt(self):
        return self.browser.find_element(*self.initialAppoint).is_displayed()

    @allure.step('Verify Appointment confirmation tab ')
    def verifyapntmntCnfrmation(self):
        return self.browser.find_element(*self.appointmentCnfrm).is_displayed()

    @allure.step('Verify Appointment Reminder tab')
    def verifyapntmntReminder(self):
        return self.browser.find_element(*self.appointmentReminder).is_displayed()

    @allure.step('Verify Rescheduling tab on Email and Sms Temaplate Dashboard Page')
    def verifyReschedulingBtn(self):
        return self.browser.find_element(*self.rescheduling).is_displayed()

    @allure.step('Verify Cancellation tab on Email and SMS Template Dashbaord Page')
    def verifyCancellationBtn(self):
        return self.browser.find_element(*self.cancellation).is_displayed()

    @allure.step('Verify Label for Email Template ')
    def verifyEmailtemplate(self):
        return self.browser.find_element(*self.emailTemplate).is_displayed()

    @allure.step('Verify Label for SMS Template ')
    def verifySmsTemplate(self):
        return self.browser.find_element(*self.smsTemplate).is_displayed()



