import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class homePageObj:

    URL = "https://aethon-test.jobrock.com"
    username = (By.XPATH, "//input[@id='i0116']")
    next_button = (By.XPATH, "//input[@id='idSIButton9']")
    password = (By.XPATH, "//input[@id='i0118']")
    signin = (By.XPATH, "//input[@id='idSIButton9']")
    stay_signed = (By.XPATH, "//input[@id='idSIButton9']")
    logo = (By.XPATH, "//a[@class='navbar-brand-logo brand brand-primary']//img[@class='img-responsive']")
    profileimg = (By.XPATH, "//li[@class='profile']//span[@class='profile-img-circle']//img")
    profilename = (By.XPATH, "//span[@class='user-label custom-v-align ng-binding']")
    profiledropdown = (By.XPATH, "//span[contains(@class,'custom-v-align fa fa-angle-down')]")
    myprofile = (By.XPATH, "//a[contains(text(),'Mijn profiel')]")
    logout = (By.XPATH, "//a[contains(text(),'Uitloggen')]")
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    calendarOption = (By.XPATH, "//span[contains(text(),'Calendars')]")
    teamCalendar = (By.XPATH, "//span[contains(text(),'Team calendar')]")
    appointmentTypes = (By.XPATH, "//span[contains(text(),'Appointment types')]")
    email_sms = (By.XPATH, "//span[contains(text(),'E-mail & SMS templates')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Load the homepage in browser')
    def load(self):
        self.browser.get(self.URL)

    @allure.step('Enter username for login')
    def enterUsername(self, un):
        time.sleep(2)
        self.browser.find_element(*self.username).send_keys(un)

    @allure.step('Click button -> Next')
    def clickNextButton(self):
        time.sleep(1)
        self.browser.find_element(*self.next_button).click()

    @allure.step('Enter password for login')
    def enterPassword(self, pswrd):
        self.browser.find_element(*self.password).send_keys(pswrd)

    @allure.step('Click button -> Sign in')
    def clickSigninButton(self):
        time.sleep(1)
        self.browser.find_element(*self.signin).click()

    @allure.step('Click Yes on stay signed button')
    def clickStaysignedIN(self):
        self.browser.find_element(*self.stay_signed).click()

    @allure.step('Verify Page Title')
    def verifyPageTitle(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.logo))
        return self.browser.title

    @allure.step('Verify Business Logo ')
    def verifyBusinesslogo(self):
        time.sleep(1)
        return self.browser.find_element(*self.logo).is_displayed()

    @allure.step('Verify Recruiter profile image')
    def verifyProfileimage(self):
        return self.browser.find_element(*self.profileimg).is_displayed()

    @allure.step('Verify Recruiter profile name ')
    def verifyProfilename(self):
        return self.browser.find_element(*self.profilename).text

    @allure.step('Verify My profile option in recruiter profile dropdown')
    def verifydropdownoption1(self):
        self.browser.find_element(*self.profiledropdown).click()
        return self.browser.find_element(*self.myprofile).text

    @allure.step('Verify Log out option in recruiter profile dropdown')
    def verifydrpodownoption2(self):
        return self.browser.find_element(*self.logout).text

    @allure.step('Verify Appointment Tab on Aethon Page')
    def verifyAppointmentab(self):
        return self.browser.find_element(*self.appointmentTab).is_displayed()

    @allure.step('Verify Calendar option in appointment tab')
    def verifyAppointment_calendar(self):
        appoint = self.browser.find_element(*self.appointmentTab)
        ActionChains(self.browser).move_to_element(appoint).perform()
        return self.browser.find_element(*self.calendarOption).is_displayed()

    @allure.step('Verify Team Calendar option in Appointment tab')
    def verifyAppointment_teamcal(self):
        return self.browser.find_element(*self.teamCalendar).is_displayed()

    @allure.step('Verify Appointment types in Appointment tab')
    def verifyAppointment_appointType(self):
        return self.browser.find_element(*self.appointmentTypes).is_displayed()

    @allure.step('Verify Email & SMS Template in appointment tab')
    def verifyAppointment_emailSms(self):
        return self.browser.find_element(*self.email_sms).is_displayed()

    @allure.step('Click appointment tab')
    def clickAppointmenttab(self):
        self.browser.find_element(*self.appointmentTab).click()







