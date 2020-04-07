from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class appCalendarDashbrdObj:
    logo = (By.XPATH, "//img[@class='logo-image-container sizing']")
    profileImg = (By.XPATH, "//img[@class='img-circle img-cu stom min-image-size sizeHeight']")
    profileName = (By.XPATH, "//span[@class='user-name-container']")
    profileDrpdwn = (By.XPATH, "//i[@class='fa fa-angle-down leftSp ace']")
    myProfile = (By.XPATH, "//a[contains(text(),'Mijn profiel')]")
    language = (By.XPATH, "//a[contains(text(),'Taal')]")
    logout = (By.XPATH, "//a[contains(text(),'Log Out')]")
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    labelCal = (By.XPATH, "//h1[@class='title-3']")
    addappCal = (By.XPATH, "//a[@class='btn blue app-data line']")
    offcDropdwn = (By.XPATH, "//div[@class='toggle']")
    agendaBtn = (By.XPATH, "//li[@class='active']/a")
    restrictionBtn = (By.XPATH, "//a[contains(text(),'Restricties instellen')]")
    blockCal = (By.XPATH, "//a[@class='orange app-data']")
    calendar = (By.XPATH, "//a[contains(text(),'Calendars')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify Logo on Calendar Dashboard Page')
    def verifycalendarLogo(self):
        return self.browser.find_element(*self.logo).is_displayed()

    @allure.step('Verify Recruiter profile image on Calendar Dashboard Page')
    def verifyProfileimage(self):
        return self.browser.find_element(*self.profileImg).is_displayed()

    @allure.step('Verify Recruiter profile name on Calendar Dashboard Page ')
    def verifyProfilename(self):
        return self.browser.find_element(*self.profileName).text

    @allure.step('Verify My profile option in recruiter profile dropdown on Calendar Dashboard Page')
    def verifydropdownoption1(self):
        self.browser.find_element(*self.profileDrpdwn).click()
        return self.browser.find_element(*self.myProfile).text

    @allure.step('Verify My profile option in recruiter profile dropdown on Calendar Dashboard Page')
    def verifydropdownoption2(self):
        return self.browser.find_element(*self.language).text

    @allure.step('Verify Log out option in recruiter profile dropdown on Calendar Dashboard Page')
    def verifydrpodownoption3(self):
        return self.browser.find_element(*self.logout).text

    @allure.step('Verify Appointment tab on Calendar Dashboard Page')
    def verifyappTab(self):
        return self.browser.find_element(*self.appointmentTab).is_displayed()

    @allure.step('Verify Label for Agenda on Calendar')
    def verifyCalLabel(self):
        return self.browser.find_element(*self.labelCal).text

    @allure.step('Verify Add Calendar option should be displayed')
    def verifyAddcalendar(self):
        return self.browser.find_element(*self.addappCal).is_displayed()

    @allure.step('Verify Action Button for Agenda ')
    def verifyAgendabtn(self):
        return self.browser.find_element(*self.agendaBtn).is_displayed()

    @allure.step('Verify Action button for Restrictions Button ')
    def verifyRestrictionbtn(self):
        return self.browser.find_element(*self.restrictionBtn).is_displayed()

    @allure.step('Verify Block Agenda option on Calndar dashboard page')
    def verifyBlockagenda(self):
        return self.browser.find_element(*self.blockCal).is_displayed()

    @allure.step('Verify Office dropdown on Appointment type Dashboard page')
    def verifyOfficedrpdwon(self):
        return self.browser.find_element(*self.offcDropdwn).is_displayed()

    @allure.step('Click Calendar from appointment dropdown .')
    def clickCalendar(self):
        appoint = self.browser.find_element(*self.appointmentTab)
        ActionChains(self.browser).move_to_element(appoint).perform()
        self.browser.find_element(*self.calendar).click()

    @allure.step('Click on Add Calendar on Calendar Dashboard Page')
    def clickAddcalendar(self):
        self.browser.find_element(*self.addappCal).click()





